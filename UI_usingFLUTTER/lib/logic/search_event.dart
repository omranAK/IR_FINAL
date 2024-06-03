part of 'search_bloc.dart';

@immutable
abstract class SearchEvent {}

final class SearchButtonPressedEvent extends SearchEvent {
  final String query;
  final int dataSetNum;
  final String mode;

  SearchButtonPressedEvent({required this.query, required this.dataSetNum,required this.mode});
}
