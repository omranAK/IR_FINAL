import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:ir_project/logic/search_bloc.dart';
import 'package:ir_project/screens/documents_screen.dart';

class SearchScreen extends StatefulWidget {
  const SearchScreen({Key? key}) : super(key: key);

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

String dropdownvalue = 'data set1';
String dropdownvalue1 = 'TF_IDF';
int ds_num = 0;

// List of items in our dropdown menu
var items = [
  'data set1',
  'data set2',
];
var items1 = ['TF_IDF', 'CLUSTRING', 'EMBDING'];

class _SearchScreenState extends State<SearchScreen> {
  TextEditingController _controller = TextEditingController();

  @override
  void initState() {
    super.initState();

    _controller.addListener(() {
      setState(() {});
    });
  }

  @override
  Widget build(BuildContext context) {
    Bloc searchBloc = BlocProvider.of<SearchBloc>(context);

    return BlocListener<SearchBloc, SearchState>(
      listener: (context, state) {
        if (state is SearchResultsLoaded) {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => DocumentsScreen(
                list: state.documents,
              ),
            ),
          );
          _controller.clear();
        }
      },
      child: Scaffold(
        body: Container(
          width: double.infinity,
          decoration: BoxDecoration(
            color: Colors.black12,
            borderRadius: BorderRadius.circular(5),
            image: DecorationImage(
              fit: BoxFit.fill,
              image: const AssetImage("assets/back.jpg"),
              colorFilter: ColorFilter.mode(
                Colors.white10.withOpacity(0.35),
                BlendMode.dstATop,
              ),
            ),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                "Search Engine ....",
                style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Colors.deepPurple.shade800),
              ),
              Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(15),
                  color: Colors.white,
                ),
                margin: const EdgeInsets.only(top: 40, left: 12, bottom: 60),
                height: 50,
                width: 150,
                child: DropdownButton(
                  borderRadius: BorderRadius.circular(15),
                  padding: const EdgeInsets.symmetric(horizontal: 15),
                  value: dropdownvalue,
                  isExpanded: true,
                  icon: const Icon(Icons.keyboard_arrow_down),
                  items: items.map((String items) {
                    return DropdownMenuItem(
                      value: items,
                      child: Text(items),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(() {
                      dropdownvalue = newValue!;
                    });
                  },
                ),
              ),
              Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(15),
                  color: Colors.white,
                ),
                margin: const EdgeInsets.only(top: 40, left: 12, bottom: 60),
                height: 50,
                width: 150,
                child: DropdownButton(
                  borderRadius: BorderRadius.circular(15),
                  padding: const EdgeInsets.symmetric(horizontal: 15),
                  value: dropdownvalue1,
                  isExpanded: true,
                  icon: const Icon(Icons.keyboard_arrow_down),
                  items: items1.map((String items) {
                    return DropdownMenuItem(
                      value: items,
                      child: Text(items),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(
                      () {
                        dropdownvalue1 = newValue!;
                      },
                    );
                  },
                ),
              ),
              Column(
                children: [
                  Container(
                    margin: const EdgeInsets.only(
                        top: 40, left: 12, right: 12, bottom: 60),
                    width: double.infinity,
                    height: 50,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(15),
                      color: Colors.white,
                    ),
                    child: TextFormField(
                      onEditingComplete: () {
                         FocusManager.instance.primaryFocus?.unfocus();
                         dropdownvalue == 'data set1' ? ds_num = 1 : ds_num = 2;
                        searchBloc.add(
                          SearchButtonPressedEvent(
                            query: _controller.text,
                            dataSetNum: ds_num,
                            mode: dropdownvalue1,
                          ),
                        );
                      },
                      controller: _controller,
                      showCursor: true,
                      cursorColor: Colors.deepPurple,
                      decoration: InputDecoration(
                        contentPadding: EdgeInsets.zero,
                        border: OutlineInputBorder(
                          borderSide: BorderSide.none,
                          borderRadius: BorderRadius.circular(15),
                        ),
                        hintText: "Search",
                        suffixIcon: const Icon(
                          Icons.search,
                          size: 25,
                          color: Colors.deepPurple,
                        ),
                        hintStyle: const TextStyle(
                          fontSize: 13,
                          color: Colors.deepPurple,
                        ),
                      ),
                      onChanged: (v) {},
                    ),
                  ),
                ],
              ),
              InkWell(
                onTap: () async {
                  // SearchRepository search = SearchRepository();
                  dropdownvalue == 'data set1' ? ds_num = 1 : ds_num = 2;

                  searchBloc.add(
                    SearchButtonPressedEvent(
                      query: _controller.text,
                      dataSetNum: ds_num,
                      mode: dropdownvalue1,
                    ),
                  );
                },
                child: Container(
                  height: 50,
                  width: 180,
                  decoration: BoxDecoration(
                    boxShadow: const [
                      BoxShadow(
                        color: Colors.deepPurple,
                      ),
                    ],
                    color: Colors.deepPurple.shade800,
                    borderRadius: BorderRadius.circular(15),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Center(
                      child: BlocBuilder<SearchBloc, SearchState>(
                        builder: (context, state) {
                          if (state is SearchResultsLoading) {
                            return const Center(
                              child: CircularProgressIndicator(),
                            );
                          }
                          return const Text(
                            "Search",
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.white,
                            ),
                          );
                        },
                      ),
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
