import 'package:flutter/material.dart';
import 'package:flutter_handson/pages/counter.dart';

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  final List<Widget> _counterPages = [
    Counter(colorLabel: "RED", counterColor: Colors.red),
    Counter(colorLabel: "PURPLE", counterColor: Colors.deepPurpleAccent),
    Counter(colorLabel: "GREEN", counterColor: Colors.lightGreen),
  ];

  int _selectedIndex = 0;

  void _updateSelectedIndex(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(
            "Flutter Hands-On",
            style: const TextStyle(color: Colors.white),
          ),
        ),
        backgroundColor: Colors.blue,
      ),
      body: Center(
        child: IndexedStack(index: _selectedIndex, children: _counterPages),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _updateSelectedIndex,
        selectedItemColor: Colors.blue,
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.add), label: "Red"),
          BottomNavigationBarItem(icon: Icon(Icons.add), label: "Purple"),
          BottomNavigationBarItem(icon: Icon(Icons.add), label: "Green"),
        ],
      ),
    );
  }
}
