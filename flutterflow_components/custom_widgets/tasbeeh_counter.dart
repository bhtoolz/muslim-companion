// Automatic FlutterFlow Custom Widget
// Widget Name: TasbeehCounter
// Dependencies required in FlutterFlow: None (Pure Flutter)

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class TasbeehCounter extends StatefulWidget {
  const TasbeehCounter({
    super.key,
    this.width,
    this.height,
    this.initialTarget = 33,
    this.primaryColor = const Color(0xFF0D3829),
    this.accentColor = const Color(0xFFC49B45),
    this.backgroundColor = const Color(0xFFFFFFFF),
    this.textColor = const Color(0xFF111815),
  });

  final double? width;
  final double? height;
  final int initialTarget;
  final Color primaryColor;
  final Color accentColor;
  final Color backgroundColor;
  final Color textColor;

  @override
  State<TasbeehCounter> createState() => _TasbeehCounterState();
}

class _TasbeehCounterState extends State<TasbeehCounter> with SingleTickerProviderStateMixin {
  late int _count;
  late int _target;
  int _laps = 0;
  int _selectedDhikrIndex = 0;

  late AnimationController _animController;
  late Animation<double> _scaleAnimation;

  final List<Map<String, String>> _dhikrList = [
    {'ar': 'سُبْحَانَ اللَّهِ', 'en': 'SubhanAllah'},
    {'ar': 'الْحَمْدُ لِلَّهِ', 'en': 'Alhamdulillah'},
    {'ar': 'اللَّهُ أَكْبَرُ', 'en': 'Allahu Akbar'},
    {'ar': 'أَسْتَغْفِرُ اللَّهَ', 'en': 'Astaghfirullah'},
    {'ar': 'لَا إِلَٰهَ إِلَّا اللَّهُ', 'en': 'La Ilaha Illallah'},
  ];

  @override
  void initState() {
    super.initState();
    _count = 0;
    _target = widget.initialTarget;

    _animController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 90),
    );

    _scaleAnimation = Tween<double>(begin: 1.0, end: 0.96).animate(
      CurvedAnimation(parent: _animController, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _animController.dispose();
    super.dispose();
  }

  void _increment() {
    HapticFeedback.lightImpact();
    _animController.forward().then((_) => _animController.reverse());

    setState(() {
      _count++;
      if (_target > 0 && _count >= _target) {
        _count = 0;
        _laps++;
        HapticFeedback.heavyImpact();
      }
    });
  }

  void _reset() {
    HapticFeedback.selectionClick();
    setState(() {
      _count = 0;
      _laps = 0;
    });
  }

  void _setTarget(int newTarget) {
    HapticFeedback.selectionClick();
    setState(() {
      _target = newTarget;
      _count = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    final progress = _target > 0 ? (_count / _target).clamp(0.0, 1.0) : 0.0;
    final currentDhikr = _dhikrList[_selectedDhikrIndex];

    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        // Dhikr Selector Carousel (Clean pill chips)
        SizedBox(
          height: 38,
          child: ListView.separated(
            scrollDirection: Axis.horizontal,
            shrinkWrap: true,
            padding: const EdgeInsets.symmetric(horizontal: 16),
            itemCount: _dhikrList.length,
            separatorBuilder: (_, __) => const SizedBox(width: 8),
            itemBuilder: (context, index) {
              final isSelected = index == _selectedDhikrIndex;
              return GestureDetector(
                onTap: () {
                  HapticFeedback.selectionClick();
                  setState(() {
                    _selectedDhikrIndex = index;
                    _count = 0;
                  });
                },
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 200),
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  decoration: BoxDecoration(
                    color: isSelected ? widget.primaryColor : widget.backgroundColor,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(
                      color: isSelected ? widget.primaryColor : Colors.black.withOpacity(0.08),
                    ),
                  ),
                  child: Text(
                    _dhikrList[index]['en']!,
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                      color: isSelected ? Colors.white : widget.textColor.withOpacity(0.7),
                    ),
                  ),
                ),
              );
            },
          ),
        ),

        const SizedBox(height: 28),

        // Dhikr Arabic Title
        Text(
          currentDhikr['ar']!,
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: 28,
            fontFamily: 'Amiri',
            fontWeight: FontWeight.w700,
            color: widget.primaryColor,
          ),
        ),

        const SizedBox(height: 24),

        // Interactive Tap Dial
        GestureDetector(
          onTap: _increment,
          child: ScaleTransition(
            scale: _scaleAnimation,
            child: Container(
              width: 240,
              height: 240,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: widget.backgroundColor,
                boxShadow: [
                  BoxShadow(
                    color: widget.primaryColor.withOpacity(0.08),
                    blurRadius: 24,
                    offset: const Offset(0, 8),
                  ),
                ],
              ),
              child: Stack(
                alignment: Alignment.center,
                children: [
                  // Circular Progress Indicator
                  SizedBox(
                    width: 220,
                    height: 220,
                    child: CircularProgressIndicator(
                      value: progress,
                      strokeWidth: 6,
                      strokeCap: StrokeCap.round,
                      backgroundColor: Colors.black.withOpacity(0.04),
                      valueColor: AlwaysStoppedAnimation<Color>(widget.accentColor),
                    ),
                  ),

                  // Inner Count Display
                  Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        '$_count',
                        style: TextStyle(
                          fontSize: 64,
                          fontWeight: FontWeight.w800,
                          letterSpacing: -1,
                          color: widget.textColor,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        'TARGET ${_target == 0 ? "∞" : "$_target"}',
                        style: TextStyle(
                          fontSize: 11,
                          letterSpacing: 1.5,
                          fontWeight: FontWeight.w700,
                          color: widget.textColor.withOpacity(0.4),
                        ),
                      ),
                      if (_laps > 0) ...[
                        const SizedBox(height: 6),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
                          decoration: BoxDecoration(
                            color: widget.accentColor.withOpacity(0.12),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Text(
                            'Cycle: $_laps',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w700,
                              color: widget.accentColor,
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),

        const SizedBox(height: 32),

        // Target Controls & Reset Bar (1-word clean buttons)
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _buildTargetChip(33),
            const SizedBox(width: 8),
            _buildTargetChip(99),
            const SizedBox(width: 8),
            _buildTargetChip(100),
            const SizedBox(width: 16),
            // Reset Button
            GestureDetector(
              onTap: _reset,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: Colors.red.shade50,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.red.shade200),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.refresh_rounded, size: 14, color: Colors.red.shade700),
                    const SizedBox(width: 4),
                    Text(
                      'Reset',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: Colors.red.shade700,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildTargetChip(int value) {
    final isSelected = _target == value;
    return GestureDetector(
      onTap: () => _setTarget(value),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        decoration: BoxDecoration(
          color: isSelected ? widget.primaryColor.withOpacity(0.1) : Colors.transparent,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected ? widget.primaryColor : Colors.black.withOpacity(0.1),
          ),
        ),
        child: Text(
          '$value',
          style: TextStyle(
            fontSize: 12,
            fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
            color: isSelected ? widget.primaryColor : widget.textColor.withOpacity(0.6),
          ),
        ),
      ),
    );
  }
}
