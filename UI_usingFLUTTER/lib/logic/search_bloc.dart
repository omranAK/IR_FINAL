// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:bloc/bloc.dart';
import 'package:ir_project/data/model/document_model.dart';
import 'package:meta/meta.dart';
import 'package:ir_project/data/repository/searc_repo.dart';
part 'search_event.dart';
part 'search_state.dart';

class SearchBloc extends Bloc<SearchEvent, SearchState> {
  SearchRepository searchRepository;
  SearchBloc(
    this.searchRepository,
  ) : super(SearchInitial()) {
    on<SearchButtonPressedEvent>(_onSearchButtonPressedEvent);
  }
  void _onSearchButtonPressedEvent(
      SearchButtonPressedEvent event, Emitter<SearchState> emit) async {
    emit(SearchResultsLoading());
    String endPoint;
    if (event.mode == 'TF_IDF') {
      print('user_query');
      endPoint = 'user_query';
    } else if (event.mode == 'CLUSTRING') {
      print('cluster');
      endPoint = 'match_to_cluster';
    } else {
      print('embding');
      endPoint = 'embedding_match';
    }
    var response = await searchRepository.getDoucument(
        event.query, event.dataSetNum, 'http://10.0.2.2:8000/api/$endPoint');
    if (response is List<DocumentModel>) {
      emit(SearchResultsLoaded(documents: response));
    } else {
      emit(SearchResultsFaild(errorMessage: 'Somthing went wrong'));
    }
  }
}
