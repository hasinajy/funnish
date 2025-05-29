import "package:flutter/material.dart";

class Counter extends StatefulWidget {
  final String colorLabel;
  final Color counterColor;

  const Counter({
    super.key,
    required this.colorLabel,
    required this.counterColor,
  });

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _counter = 0;

  void _resetCounter() {
    setState(() {
      _counter = 0;
    });
  }

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.grey[200],
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            "${widget.colorLabel} COUNTER",
            style: TextStyle(
              color: Colors.grey[800],
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
          Text(
            "$_counter",
            style: TextStyle(color: widget.counterColor, fontSize: 96),
          ),
          Row(
            mainAxisSize: MainAxisSize.min,
            spacing: 18,
            children: [
              ElevatedButton(
                onPressed: _resetCounter,
                child: Text(
                  "Reset",
                  style: TextStyle(color: Colors.grey[600], fontSize: 16),
                ),
              ),
              ElevatedButton(
                onPressed: _incrementCounter,
                child: Text(
                  "Increment",
                  style: TextStyle(color: Colors.grey[600], fontSize: 16),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
