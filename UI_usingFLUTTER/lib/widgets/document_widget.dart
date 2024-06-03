import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class DocumentWidget extends StatelessWidget {
  String title;
  String description;

  DocumentWidget({
    Key? key,
    required this.title,
    required this.description,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    return Container(
      height: size.height / 3.1,
      decoration: const BoxDecoration(color: Colors.white70
          //  borderRadius: BorderRadius.circular(15),
          ),
      child: Padding(
        padding: const EdgeInsets.only(top: 15, left: 15, right: 15),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
                flex: 1,
                child: Text(
                  title,
                  style: const TextStyle(
                      fontWeight: FontWeight.w700, fontSize: 14),
                )),
            Expanded(
                flex: 4,
                child: SizedBox(
                    width: size.width / 3,
                    child: Text(
                      description,
                      style: const TextStyle(
                        fontWeight: FontWeight.w500,
                        fontSize: 14,
                      ),
                      // maxLines: 3,
                    ))),
          ],
        ),
      ),
    );
  }
}
