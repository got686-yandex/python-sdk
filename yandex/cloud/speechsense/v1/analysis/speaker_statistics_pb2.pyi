"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import yandex.cloud.speechsense.v1.analysis.statistics_common_pb2
import yandex.cloud.speechsense.v1.analysis.utterance_statistics_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SpeakerStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPEAKER_TAG_FIELD_NUMBER: builtins.int
    COMPLETE_STATISTICS_FIELD_NUMBER: builtins.int
    WORDS_PER_UTTERANCE_FIELD_NUMBER: builtins.int
    LETTERS_PER_UTTERANCE_FIELD_NUMBER: builtins.int
    UTTERANCE_COUNT_FIELD_NUMBER: builtins.int
    UTTERANCE_DURATION_ESTIMATION_FIELD_NUMBER: builtins.int
    speaker_tag: builtins.str
    """Speaker tag"""
    utterance_count: builtins.int
    """Number of utterances"""
    @property
    def complete_statistics(self) -> yandex.cloud.speechsense.v1.analysis.utterance_statistics_pb2.UtteranceStatistics:
        """analysis of all phrases in format of single utterance"""

    @property
    def words_per_utterance(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics:
        """Descriptive statistics for words per utterance distribution"""

    @property
    def letters_per_utterance(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics:
        """Descriptive statistics for letters per utterance distribution"""

    @property
    def utterance_duration_estimation(self) -> yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics:
        """Descriptive statistics for utterance duration distribution"""

    def __init__(
        self,
        *,
        speaker_tag: builtins.str = ...,
        complete_statistics: yandex.cloud.speechsense.v1.analysis.utterance_statistics_pb2.UtteranceStatistics | None = ...,
        words_per_utterance: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics | None = ...,
        letters_per_utterance: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics | None = ...,
        utterance_count: builtins.int = ...,
        utterance_duration_estimation: yandex.cloud.speechsense.v1.analysis.statistics_common_pb2.DescriptiveStatistics | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["complete_statistics", b"complete_statistics", "letters_per_utterance", b"letters_per_utterance", "utterance_duration_estimation", b"utterance_duration_estimation", "words_per_utterance", b"words_per_utterance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["complete_statistics", b"complete_statistics", "letters_per_utterance", b"letters_per_utterance", "speaker_tag", b"speaker_tag", "utterance_count", b"utterance_count", "utterance_duration_estimation", b"utterance_duration_estimation", "words_per_utterance", b"words_per_utterance"]) -> None: ...

global___SpeakerStatistics = SpeakerStatistics