import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ir_project/data/repository/searc_repo.dart';
import 'package:ir_project/logic/search_bloc.dart';
import 'package:ir_project/screens/search_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => SearchBloc(SearchRepository()),
      child: const MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'Search Engine',
        home: SearchScreen(),
      ),
    );
  }
}
