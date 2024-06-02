import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:ir_project/data/model/document_model.dart';

class SearchRepository {
  Future getDoucument(String qry, int ds_num, String url) async {
    var headers = {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
      //'Access-Control-Allow-Origin': 'http://10.0.2.2:8000/api/user_query'
    };
    var request =
        http.Request('POST', Uri.parse(url));
    request.body = json.encode({"ds_num": ds_num, "qry": qry});
    request.headers.addAll(headers);

    var response = await request.send();
    final respStr = await response.stream.bytesToString();
    List decodedList = json.decode(respStr);
    List<DocumentModel> documetnList = [];

    if (response.statusCode == 200) {
      decodedList.forEach((element) {
        documetnList.add(
          DocumentModel(
            element['doc_id'],
            element['text'],
          ),
        );
      });
      return documetnList;
      // List<String>list=responseBody.split('"}');
      // return list;
    } else {
      print(response.reasonPhrase);
    }
  }
}
