import 'package:flutter/material.dart';


class ButtonWidget extends StatelessWidget {
  final String title;

  final GestureTapCallback onTap;

  Color color;

  ButtonWidget({
    Key? key,
    required this.title,
    this.color = Colors.deepPurple,
    required this.onTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    return InkWell(
      onTap: onTap,
      child: Container(
        height: 40,
        constraints: BoxConstraints(
          minWidth: 120,
        ),
        decoration: BoxDecoration(
          boxShadow: [
            BoxShadow(
              color: Colors.deepPurple,
            ),
          ],
          color: color,
          borderRadius: BorderRadius.circular(15),
        ),
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Center(
            child: Text(
              title,
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 13,
                color: Colors.white,
              ),
            ),
          ),
        ),
      ),
    );
  }
}
