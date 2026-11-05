// Automatic FlutterFlow Custom Action
// Action Name: getPrayerTimes
// Return Type: <JSON> (Dynamic Map)
// Dependencies in FlutterFlow:
// http: ^1.2.0
// intl: ^0.19.0

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

Future<dynamic> getPrayerTimes(
  double latitude,
  double longitude,
  int? calculationMethod, // default: 4 (Umm Al-Qura) or 2 (ISNA)
) async {
  try {
    final method = calculationMethod ?? 4;
    final now = DateTime.now();
    final dateStr = DateFormat('dd-MM-yyyy').format(now);

    final url = Uri.parse(
      'https://api.aladhan.com/v1/timings/$dateStr?latitude=$latitude&longitude=$longitude&method=$method',
    );

    final response = await http.get(url).timeout(const Duration(seconds: 8));

    if (response.statusCode != 200) {
      return {'success': false, 'error': 'API returned ${response.statusCode}'};
    }

    final data = jsonDecode(response.body);
    final timings = data['data']['timings'];
    final meta = data['data']['meta'];
    final hijri = data['data']['date']['hijri'];

    // Cleaned 5 Daily Prayers + Sunrise
    final rawPrayers = <String, String>{
      'Fajr': timings['Fajr'],
      'Sunrise': timings['Sunrise'],
      'Dhuhr': timings['Dhuhr'],
      'Asr': timings['Asr'],
      'Maghrib': timings['Maghrib'],
      'Isha': timings['Isha'],
    };

    // Calculate current prayer and next prayer with countdown
    String nextPrayerName = 'Fajr';
    DateTime? nextPrayerTime;
    Duration remaining = Duration.zero;

    final parsedPrayerTimes = <String, DateTime>{};

    for (var entry in rawPrayers.entries) {
      final timeParts = entry.value.split(':');
      final hour = int.parse(timeParts[0]);
      final minute = int.parse(timeParts[1]);

      final pTime = DateTime(now.year, now.month, now.day, hour, minute);
      parsedPrayerTimes[entry.key] = pTime;
    }

    // Determine next prayer
    for (var entry in parsedPrayerTimes.entries) {
      if (entry.key == 'Sunrise') continue; // Sunrise is not a fard prayer
      if (entry.value.isAfter(now)) {
        nextPrayerName = entry.key;
        nextPrayerTime = entry.value;
        remaining = nextPrayerTime.difference(now);
        break;
      }
    }

    // If all today's prayers passed, next is tomorrow's Fajr
    if (nextPrayerTime == null) {
      nextPrayerName = 'Fajr';
      final fajrParts = rawPrayers['Fajr']!.split(':');
      final tomorrow = now.add(const Duration(days: 1));
      nextPrayerTime = DateTime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        int.parse(fajrParts[0]),
        int.parse(fajrParts[1]),
      );
      remaining = nextPrayerTime.difference(now);
    }

    // Format Countdown HH:mm:ss
    final hours = remaining.inHours.toString().padLeft(2, '0');
    final minutes = (remaining.inMinutes % 60).toString().padLeft(2, '0');
    final seconds = (remaining.inSeconds % 60).toString().padLeft(2, '0');
    final countdownString = '$hours:$minutes:$seconds';

    return {
      'success': true,
      'timings': rawPrayers,
      'nextPrayer': {
        'name': nextPrayerName,
        'time': rawPrayers[nextPrayerName],
        'countdown': countdownString,
        'remainingSeconds': remaining.inSeconds,
      },
      'hijri': {
        'day': hijri['day'],
        'monthEn': hijri['month']['en'],
        'monthAr': hijri['month']['ar'],
        'year': hijri['year'],
      },
      'timezone': meta['timezone'],
    };
  } catch (e) {
    return {'success': false, 'error': e.toString()};
  }
}
