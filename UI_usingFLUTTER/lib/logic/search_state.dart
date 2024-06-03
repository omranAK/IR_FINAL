part of 'search_bloc.dart';

@immutable
abstract class SearchState {}

class SearchInitial extends SearchState {}

final class SearchResultsLoaded extends SearchState {
  final List<DocumentModel> documents;

  SearchResultsLoaded({required this.documents});
}

final class SearchResultsLoading extends SearchState {}

final class SearchResultsFaild extends SearchState {
  final String errorMessage;

  SearchResultsFaild({required this.errorMessage});
}
