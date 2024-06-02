// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ir_project/data/model/document_model.dart';
import '../widgets/button_widget.dart';

class DocumentsScreen extends StatefulWidget {
  final List<DocumentModel> list;
  const DocumentsScreen({
    Key? key,
    required this.list,
  }) : super(key: key);

  @override
  State<DocumentsScreen> createState() => _DocumentsScreenState();
}

class _DocumentsScreenState extends State<DocumentsScreen> {
  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.only(top: 50.0, left: 8, right: 8),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text(
                    "Query Results",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.deepPurple,
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(
                        top: 15.0, right: 8.0, bottom: 15),
                    child: ButtonWidget(
                        title: "back",
                        onTap: () {
                          Navigator.pop(context);
                        }),
                  ),
                ],
              ),
              SizedBox(
                height: size.height / 1.2,
                width: size.width,
                child: ListView.builder(
                  scrollDirection: Axis.vertical,
                  itemCount: widget.list.length,
                  itemBuilder: (context, index) => SizedBox(
                    
                    width: double.infinity,
                    child: Column(
                      children: [
                        Text(
                          '${widget.list[index].doc_id}',
                          style: const TextStyle(fontSize: 20),
                        ),
                        Text(widget.list[index].text,style:const  TextStyle(fontWeight: FontWeight.w500),),
                        const Divider(
                          color: Colors.black,
                          thickness: 2,
                        )
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
