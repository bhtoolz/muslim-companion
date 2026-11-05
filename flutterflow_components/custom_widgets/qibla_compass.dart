// Automatic FlutterFlow Custom Widget
// Widget Name: QiblaCompass
// Dependencies required in FlutterFlow:
// flutter_compass: ^0.8.0
// sensors_plus: ^5.0.1

import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_compass/flutter_compass.dart';

class QiblaCompass extends StatefulWidget {
  const QiblaCompass({
    super.key,
    this.width,
    this.height,
    required this.userLatitude,
    required this.userLongitude,
    this.primaryColor = const Color(0xFF0D3829),
    this.accentColor = const Color(0xFFC49B45),
    this.surfaceColor = const Color(0xFFFFFFFF),
    this.textColor = const Color(0xFF111815),
  });

  final double? width;
  final double? height;
  final double userLatitude;
  final double userLongitude;
  final Color primaryColor;
  final Color accentColor;
  final Color surfaceColor;
  final Color textColor;

  @override
  State<QiblaCompass> createState() => _QiblaCompassState();
}

class _QiblaCompassState extends State<QiblaCompass> {
  // Coordinates of Kaaba, Makkah
  static const double _kaabaLat = 21.422487;
  static const double _kaabaLng = 39.826206;

  double _qiblaBearing = 0.0;
  double? _deviceHeading;
  bool _hasVibrated = false;

  @override
  void initState() {
    super.initState();
    _qiblaBearing = _calculateQiblaBearing(widget.userLatitude, widget.userLongitude);
    _listenToCompass();
  }

  @override
  void didUpdateWidget(covariant QiblaCompass oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.userLatitude != widget.userLatitude ||
        oldWidget.userLongitude != widget.userLongitude) {
      setState(() {
        _qiblaBearing = _calculateQiblaBearing(widget.userLatitude, widget.userLongitude);
      });
    }
  }

  void _listenToCompass() {
    FlutterCompass.events?.listen((CompassEvent event) {
      if (!mounted) return;
      final heading = event.heading;
      if (heading == null) return;

      setState(() {
        _deviceHeading = heading;
      });

      // Difference between heading and Qibla bearing
      final diff = ((heading - _qiblaBearing).abs()) % 360;
      final isAligned = diff < 2.5 || diff > 357.5;

      if (isAligned && !_hasVibrated) {
        HapticFeedback.mediumImpact();
        _hasVibrated = true;
      } else if (!isAligned) {
        _hasVibrated = false;
      }
    });
  }

  double _calculateQiblaBearing(double lat, double lng) {
    final phi1 = lat * (math.pi / 180.0);
    final phi2 = _kaabaLat * (math.pi / 180.0);
    final deltaLambda = (_kaabaLng - lng) * (math.pi / 180.0);

    final y = math.sin(deltaLambda);
    final x = math.cos(phi1) * math.tan(phi2) - math.sin(phi1) * math.cos(deltaLambda);
    final bearingRad = math.atan2(y, x);

    double bearingDeg = bearingRad * (180.0 / math.pi);
    return (bearingDeg + 360.0) % 360.0;
  }

  @override
  Widget build(BuildContext context) {
    final size = math.min(widget.width ?? 320.0, widget.height ?? 320.0);
    final heading = _deviceHeading ?? 0.0;
    final diff = ((heading - _qiblaBearing).abs()) % 360;
    final isAligned = diff < 3.0 || diff > 357.0;

    return Center(
      child: SizedBox(
        width: size,
        height: size,
        child: Stack(
          alignment: Alignment.center,
          children: [
            // Outer dial container
            Container(
              width: size,
              height: size,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: widget.surfaceColor,
                boxShadow: [
                  BoxShadow(
                    color: isAligned
                        ? widget.accentColor.withOpacity(0.35)
                        : Colors.black.withOpacity(0.06),
                    blurRadius: isAligned ? 28 : 16,
                    spreadRadius: isAligned ? 4 : 0,
                    offset: const Offset(0, 4),
                  ),
                ],
                border: Border.all(
                  color: isAligned ? widget.accentColor : Colors.black.withOpacity(0.08),
                  width: isAligned ? 2.5 : 1.2,
                ),
              ),
            ),

            // Rotating Compass Ring (North, East, South, West & Ticks)
            Transform.rotate(
              angle: (heading * (math.pi / 180.0) * -1),
              child: CustomPaint(
                size: Size(size, size),
                painter: _CompassDialPainter(
                  accentColor: widget.accentColor,
                  dialColor: widget.textColor.withOpacity(0.35),
                  northColor: const Color(0xFFE53935),
                ),
              ),
            ),

            // Qibla Indicator Needle (Points directly to Makkah relative to phone heading)
            Transform.rotate(
              angle: ((_qiblaBearing - heading) * (math.pi / 180.0)),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // Gold Kaaba Indicator Head
                  Container(
                    width: 38,
                    height: 38,
                    decoration: BoxDecoration(
                      color: isAligned ? widget.accentColor : widget.primaryColor,
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: widget.accentColor.withOpacity(0.4),
                          blurRadius: 10,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    child: const Icon(
                      Icons.navigation_rounded,
                      color: Colors.white,
                      size: 22,
                    ),
                  ),
                  SizedBox(height: (size / 2) - 38),
                ],
              ),
            ),

            // Center Info Badge
            Container(
              width: 88,
              height: 88,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: widget.surfaceColor,
                border: Border.all(
                  color: isAligned ? widget.accentColor : Colors.black.withOpacity(0.08),
                  width: 1.5,
                ),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    '${_qiblaBearing.round()}°',
                    style: TextStyle(
                      fontFamily: 'Plus Jakarta Sans',
                      fontSize: 20,
                      fontWeight: FontWeight.w700,
                      color: isAligned ? widget.accentColor : widget.textColor,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    isAligned ? 'ALIGNED' : 'QIBLA',
                    style: TextStyle(
                      letterSpacing: 1.5,
                      fontSize: 10,
                      fontWeight: FontWeight.w700,
                      color: isAligned ? widget.accentColor : widget.textColor.withOpacity(0.5),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _CompassDialPainter extends CustomPainter {
  final Color accentColor;
  final Color dialColor;
  final Color northColor;

  _CompassDialPainter({
    required this.accentColor,
    required this.dialColor,
    required this.northColor,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.width / 2;

    final tickPaint = Paint()
      ..strokeCap = StrokeCap.round
      ..strokeWidth = 1.2;

    for (int i = 0; i < 72; i++) {
      final angle = (i * 5) * (math.pi / 180.0);
      final isMajor = i % 18 == 0; // 0, 90, 180, 270 (N, E, S, W)
      final isMedium = i % 6 == 0;

      final tickLength = isMajor ? 14.0 : (isMedium ? 9.0 : 5.0);

      tickPaint.color = i == 0 ? northColor : (isMajor ? accentColor : dialColor);
      tickPaint.strokeWidth = isMajor ? 2.2 : (isMedium ? 1.4 : 0.9);

      final outerX = center.dx + (radius - 12) * math.cos(angle);
      final outerY = center.dy + (radius - 12) * math.sin(angle);
      final innerX = center.dx + (radius - 12 - tickLength) * math.cos(angle);
      final innerY = center.dy + (radius - 12 - tickLength) * math.sin(angle);

      canvas.drawLine(Offset(innerX, innerY), Offset(outerX, outerY), tickPaint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
