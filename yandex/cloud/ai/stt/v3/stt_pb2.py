# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/stt/v3/stt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n yandex/cloud/ai/stt/v3/stt.proto\x12\x10speechkit.stt.v3\"\xe2\x03\n\x18TextNormalizationOptions\x12X\n\x12text_normalization\x18\x01 \x01(\x0e\x32<.speechkit.stt.v3.TextNormalizationOptions.TextNormalization\x12\x18\n\x10profanity_filter\x18\x02 \x01(\x08\x12\x17\n\x0fliterature_text\x18\x03 \x01(\x08\x12]\n\x15phone_formatting_mode\x18\x04 \x01(\x0e\x32>.speechkit.stt.v3.TextNormalizationOptions.PhoneFormattingMode\"x\n\x11TextNormalization\x12\"\n\x1eTEXT_NORMALIZATION_UNSPECIFIED\x10\x00\x12\x1e\n\x1aTEXT_NORMALIZATION_ENABLED\x10\x01\x12\x1f\n\x1bTEXT_NORMALIZATION_DISABLED\x10\x02\"`\n\x13PhoneFormattingMode\x12%\n!PHONE_FORMATTING_MODE_UNSPECIFIED\x10\x00\x12\"\n\x1ePHONE_FORMATTING_MODE_DISABLED\x10\x01\"\xce\x01\n\x14\x44\x65\x66\x61ultEouClassifier\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.speechkit.stt.v3.DefaultEouClassifier.EouSensitivity\x12\'\n\x1fmax_pause_between_words_hint_ms\x18\x02 \x01(\x03\"H\n\x0e\x45ouSensitivity\x12\x1f\n\x1b\x45OU_SENSITIVITY_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\x08\n\x04HIGH\x10\x02\"\x17\n\x15\x45xternalEouClassifier\"\xb2\x01\n\x14\x45ouClassifierOptions\x12\x44\n\x12\x64\x65\x66\x61ult_classifier\x18\x01 \x01(\x0b\x32&.speechkit.stt.v3.DefaultEouClassifierH\x00\x12\x46\n\x13\x65xternal_classifier\x18\x02 \x01(\x0b\x32\'.speechkit.stt.v3.ExternalEouClassifierH\x00\x42\x0c\n\nClassifier\"\xd3\x01\n\x15RecognitionClassifier\x12\x12\n\nclassifier\x18\x01 \x01(\t\x12\x45\n\x08triggers\x18\x02 \x03(\x0e\x32\x33.speechkit.stt.v3.RecognitionClassifier.TriggerType\"_\n\x0bTriggerType\x12 \n\x18TRIGGER_TYPE_UNSPECIFIED\x10\x00\x1a\x02\x08\x01\x12\x10\n\x0cON_UTTERANCE\x10\x01\x12\x0c\n\x08ON_FINAL\x10\x02\x12\x0e\n\nON_PARTIAL\x10\x03\"\\\n\x1cRecognitionClassifierOptions\x12<\n\x0b\x63lassifiers\x18\x01 \x03(\x0b\x32\'.speechkit.stt.v3.RecognitionClassifier\"\x88\x01\n\x15SpeechAnalysisOptions\x12\x1f\n\x17\x65nable_speaker_analysis\x18\x01 \x01(\x08\x12$\n\x1c\x65nable_conversation_analysis\x18\x02 \x01(\x08\x12(\n descriptive_statistics_quantiles\x18\x03 \x03(\x01\"\xc7\x01\n\x08RawAudio\x12@\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32(.speechkit.stt.v3.RawAudio.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x03\x12\x1b\n\x13\x61udio_channel_count\x18\x03 \x01(\x03\"A\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x10\n\x0cLINEAR16_PCM\x10\x01\"\xbf\x01\n\x0e\x43ontainerAudio\x12Q\n\x14\x63ontainer_audio_type\x18\x01 \x01(\x0e\x32\x33.speechkit.stt.v3.ContainerAudio.ContainerAudioType\"Z\n\x12\x43ontainerAudioType\x12$\n CONTAINER_AUDIO_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03WAV\x10\x01\x12\x0c\n\x08OGG_OPUS\x10\x02\x12\x07\n\x03MP3\x10\x03\"\x91\x01\n\x12\x41udioFormatOptions\x12/\n\traw_audio\x18\x01 \x01(\x0b\x32\x1a.speechkit.stt.v3.RawAudioH\x00\x12;\n\x0f\x63ontainer_audio\x18\x02 \x01(\x0b\x32 .speechkit.stt.v3.ContainerAudioH\x00\x42\r\n\x0b\x41udioFormat\"\xf7\x01\n\x1aLanguageRestrictionOptions\x12^\n\x10restriction_type\x18\x01 \x01(\x0e\x32\x44.speechkit.stt.v3.LanguageRestrictionOptions.LanguageRestrictionType\x12\x15\n\rlanguage_code\x18\x02 \x03(\t\"b\n\x17LanguageRestrictionType\x12)\n%LANGUAGE_RESTRICTION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tWHITELIST\x10\x01\x12\r\n\tBLACKLIST\x10\x02\"\xb2\x03\n\x17RecognitionModelOptions\x12\r\n\x05model\x18\x01 \x01(\t\x12:\n\x0c\x61udio_format\x18\x02 \x01(\x0b\x32$.speechkit.stt.v3.AudioFormatOptions\x12\x46\n\x12text_normalization\x18\x03 \x01(\x0b\x32*.speechkit.stt.v3.TextNormalizationOptions\x12J\n\x14language_restriction\x18\x04 \x01(\x0b\x32,.speechkit.stt.v3.LanguageRestrictionOptions\x12\\\n\x15\x61udio_processing_type\x18\x05 \x01(\x0e\x32=.speechkit.stt.v3.RecognitionModelOptions.AudioProcessingType\"Z\n\x13\x41udioProcessingType\x12%\n!AUDIO_PROCESSING_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tREAL_TIME\x10\x01\x12\r\n\tFULL_DATA\x10\x02\"\xde\x01\n\x16SpeakerLabelingOptions\x12R\n\x10speaker_labeling\x18\x01 \x01(\x0e\x32\x38.speechkit.stt.v3.SpeakerLabelingOptions.SpeakerLabeling\"p\n\x0fSpeakerLabeling\x12 \n\x1cSPEAKER_LABELING_UNSPECIFIED\x10\x00\x12\x1c\n\x18SPEAKER_LABELING_ENABLED\x10\x01\x12\x1d\n\x19SPEAKER_LABELING_DISABLED\x10\x02\"\xee\x02\n\x10StreamingOptions\x12\x44\n\x11recognition_model\x18\x01 \x01(\x0b\x32).speechkit.stt.v3.RecognitionModelOptions\x12>\n\x0e\x65ou_classifier\x18\x02 \x01(\x0b\x32&.speechkit.stt.v3.EouClassifierOptions\x12N\n\x16recognition_classifier\x18\x03 \x01(\x0b\x32..speechkit.stt.v3.RecognitionClassifierOptions\x12@\n\x0fspeech_analysis\x18\x04 \x01(\x0b\x32\'.speechkit.stt.v3.SpeechAnalysisOptions\x12\x42\n\x10speaker_labeling\x18\x05 \x01(\x0b\x32(.speechkit.stt.v3.SpeakerLabelingOptions\"\x1a\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"#\n\x0cSilenceChunk\x12\x13\n\x0b\x64uration_ms\x18\x01 \x01(\x03\"\x05\n\x03\x45ou\"\xe8\x01\n\x10StreamingRequest\x12=\n\x0fsession_options\x18\x01 \x01(\x0b\x32\".speechkit.stt.v3.StreamingOptionsH\x00\x12-\n\x05\x63hunk\x18\x02 \x01(\x0b\x32\x1c.speechkit.stt.v3.AudioChunkH\x00\x12\x37\n\rsilence_chunk\x18\x03 \x01(\x0b\x32\x1e.speechkit.stt.v3.SilenceChunkH\x00\x12$\n\x03\x65ou\x18\x04 \x01(\x0b\x32\x15.speechkit.stt.v3.EouH\x00\x42\x07\n\x05\x45vent\"\xe3\x02\n\x14RecognizeFileRequest\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x12\x44\n\x11recognition_model\x18\x03 \x01(\x0b\x32).speechkit.stt.v3.RecognitionModelOptions\x12N\n\x16recognition_classifier\x18\x04 \x01(\x0b\x32..speechkit.stt.v3.RecognitionClassifierOptions\x12@\n\x0fspeech_analysis\x18\x05 \x01(\x0b\x32\'.speechkit.stt.v3.SpeechAnalysisOptions\x12\x42\n\x10speaker_labeling\x18\x06 \x01(\x0b\x32(.speechkit.stt.v3.SpeakerLabelingOptionsB\r\n\x0b\x41udioSource\"@\n\x04Word\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\"@\n\x12LanguageEstimation\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x13\n\x0bprobability\x18\x02 \x01(\x01\"\xbb\x01\n\x0b\x41lternative\x12%\n\x05words\x18\x01 \x03(\x0b\x32\x16.speechkit.stt.v3.Word\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x15\n\rstart_time_ms\x18\x03 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x04 \x01(\x03\x12\x12\n\nconfidence\x18\x05 \x01(\x01\x12\x37\n\tlanguages\x18\x06 \x03(\x0b\x32$.speechkit.stt.v3.LanguageEstimation\"\x1c\n\tEouUpdate\x12\x0f\n\x07time_ms\x18\x02 \x01(\x03\"a\n\x11\x41lternativeUpdate\x12\x33\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x1d.speechkit.stt.v3.Alternative\x12\x17\n\x0b\x63hannel_tag\x18\x02 \x01(\tB\x02\x18\x01\"\x99\x01\n\x0c\x41udioCursors\x12\x18\n\x10received_data_ms\x18\x01 \x01(\x03\x12\x15\n\rreset_time_ms\x18\x02 \x01(\x03\x12\x17\n\x0fpartial_time_ms\x18\x03 \x01(\x03\x12\x15\n\rfinal_time_ms\x18\x04 \x01(\x03\x12\x13\n\x0b\x66inal_index\x18\x05 \x01(\x03\x12\x13\n\x0b\x65ou_time_ms\x18\x06 \x01(\x03\"n\n\x0f\x46inalRefinement\x12\x13\n\x0b\x66inal_index\x18\x01 \x01(\x03\x12>\n\x0fnormalized_text\x18\x02 \x01(\x0b\x32#.speechkit.stt.v3.AlternativeUpdateH\x00\x42\x06\n\x04Type\"L\n\nStatusCode\x12-\n\tcode_type\x18\x01 \x01(\x0e\x32\x1a.speechkit.stt.v3.CodeType\x12\x0f\n\x07message\x18\x02 \x01(\t\"4\n\x0bSessionUuid\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\x0fuser_request_id\x18\x02 \x01(\t\"K\n\x0fPhraseHighlight\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\"?\n\x1aRecognitionClassifierLabel\x12\r\n\x05label\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x01\"\xa6\x01\n\x1bRecognitionClassifierResult\x12\x12\n\nclassifier\x18\x01 \x01(\t\x12\x35\n\nhighlights\x18\x02 \x03(\x0b\x32!.speechkit.stt.v3.PhraseHighlight\x12<\n\x06labels\x18\x03 \x03(\x0b\x32,.speechkit.stt.v3.RecognitionClassifierLabel\"\xc7\x02\n\x1bRecognitionClassifierUpdate\x12M\n\x0bwindow_type\x18\x01 \x01(\x0e\x32\x38.speechkit.stt.v3.RecognitionClassifierUpdate.WindowType\x12\x15\n\rstart_time_ms\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x03 \x01(\x03\x12H\n\x11\x63lassifier_result\x18\x04 \x01(\x0b\x32-.speechkit.stt.v3.RecognitionClassifierResult\"c\n\nWindowType\x12\x1f\n\x17WINDOW_TYPE_UNSPECIFIED\x10\x00\x1a\x02\x08\x01\x12\x12\n\x0eLAST_UTTERANCE\x10\x01\x12\x0e\n\nLAST_FINAL\x10\x02\x12\x10\n\x0cLAST_PARTIAL\x10\x03\"\xbb\x01\n\x15\x44\x65scriptiveStatistics\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\x0c\n\x04mean\x18\x03 \x01(\x01\x12\x0b\n\x03std\x18\x04 \x01(\x01\x12\x43\n\tquantiles\x18\x05 \x03(\x0b\x32\x30.speechkit.stt.v3.DescriptiveStatistics.Quantile\x1a(\n\x08Quantile\x12\r\n\x05level\x18\x01 \x01(\x01\x12\r\n\x05value\x18\x02 \x01(\x01\"D\n\x16\x41udioSegmentBoundaries\x12\x15\n\rstart_time_ms\x18\x01 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x02 \x01(\x03\"\x87\x06\n\x0fSpeakerAnalysis\x12\x13\n\x0bspeaker_tag\x18\x01 \x01(\t\x12\x41\n\x0bwindow_type\x18\x02 \x01(\x0e\x32,.speechkit.stt.v3.SpeakerAnalysis.WindowType\x12\x43\n\x11speech_boundaries\x18\x03 \x01(\x0b\x32(.speechkit.stt.v3.AudioSegmentBoundaries\x12\x17\n\x0ftotal_speech_ms\x18\x04 \x01(\x03\x12\x14\n\x0cspeech_ratio\x18\x05 \x01(\x01\x12\x18\n\x10total_silence_ms\x18\x06 \x01(\x03\x12\x15\n\rsilence_ratio\x18\x07 \x01(\x01\x12\x13\n\x0bwords_count\x18\x08 \x01(\x03\x12\x15\n\rletters_count\x18\t \x01(\x03\x12\x41\n\x10words_per_second\x18\n \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12\x43\n\x12letters_per_second\x18\x0b \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12\x44\n\x13words_per_utterance\x18\x0c \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12\x46\n\x15letters_per_utterance\x18\r \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12\x17\n\x0futterance_count\x18\x0e \x01(\x03\x12N\n\x1dutterance_duration_estimation\x18\x0f \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\"L\n\nWindowType\x12\x1f\n\x17WINDOW_TYPE_UNSPECIFIED\x10\x00\x1a\x02\x08\x01\x12\t\n\x05TOTAL\x10\x01\x12\x12\n\x0eLAST_UTTERANCE\x10\x02\"\x85\x06\n\x14\x43onversationAnalysis\x12I\n\x17\x63onversation_boundaries\x18\x01 \x01(\x0b\x32(.speechkit.stt.v3.AudioSegmentBoundaries\x12.\n&total_simultaneous_silence_duration_ms\x18\x02 \x01(\x03\x12(\n total_simultaneous_silence_ratio\x18\x03 \x01(\x01\x12Y\n(simultaneous_silence_duration_estimation\x18\x04 \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12-\n%total_simultaneous_speech_duration_ms\x18\x05 \x01(\x03\x12\'\n\x1ftotal_simultaneous_speech_ratio\x18\x06 \x01(\x01\x12X\n\'simultaneous_speech_duration_estimation\x18\x07 \x01(\x0b\x32\'.speechkit.stt.v3.DescriptiveStatistics\x12W\n\x12speaker_interrupts\x18\x08 \x03(\x0b\x32;.speechkit.stt.v3.ConversationAnalysis.InterruptsEvaluation\x12 \n\x18total_speech_duration_ms\x18\t \x01(\x03\x12\x1a\n\x12total_speech_ratio\x18\n \x01(\x01\x1a\xa3\x01\n\x14InterruptsEvaluation\x12\x13\n\x0bspeaker_tag\x18\x01 \x01(\t\x12\x18\n\x10interrupts_count\x18\x02 \x01(\x03\x12\x1e\n\x16interrupts_duration_ms\x18\x03 \x01(\x03\x12<\n\ninterrupts\x18\x04 \x03(\x0b\x32(.speechkit.stt.v3.AudioSegmentBoundaries\"\xa5\x05\n\x11StreamingResponse\x12\x33\n\x0csession_uuid\x18\x01 \x01(\x0b\x32\x1d.speechkit.stt.v3.SessionUuid\x12\x35\n\raudio_cursors\x18\x02 \x01(\x0b\x32\x1e.speechkit.stt.v3.AudioCursors\x12\x1d\n\x15response_wall_time_ms\x18\x03 \x01(\x03\x12\x36\n\x07partial\x18\x04 \x01(\x0b\x32#.speechkit.stt.v3.AlternativeUpdateH\x00\x12\x34\n\x05\x66inal\x18\x05 \x01(\x0b\x32#.speechkit.stt.v3.AlternativeUpdateH\x00\x12\x31\n\neou_update\x18\x06 \x01(\x0b\x32\x1b.speechkit.stt.v3.EouUpdateH\x00\x12=\n\x10\x66inal_refinement\x18\x07 \x01(\x0b\x32!.speechkit.stt.v3.FinalRefinementH\x00\x12\x33\n\x0bstatus_code\x18\x08 \x01(\x0b\x32\x1c.speechkit.stt.v3.StatusCodeH\x00\x12J\n\x11\x63lassifier_update\x18\n \x01(\x0b\x32-.speechkit.stt.v3.RecognitionClassifierUpdateH\x00\x12=\n\x10speaker_analysis\x18\x0b \x01(\x0b\x32!.speechkit.stt.v3.SpeakerAnalysisH\x00\x12G\n\x15\x63onversation_analysis\x18\x0c \x01(\x0b\x32&.speechkit.stt.v3.ConversationAnalysisH\x00\x12\x13\n\x0b\x63hannel_tag\x18\t \x01(\tB\x07\n\x05\x45vent*O\n\x08\x43odeType\x12\x1d\n\x15\x43ODE_TYPE_UNSPECIFIED\x10\x00\x1a\x02\x08\x01\x12\x0b\n\x07WORKING\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\n\n\x06\x43LOSED\x10\x03\x42\\\n\x1ayandex.cloud.api.ai.stt.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/stt/v3;sttb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.ai.stt.v3.stt_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032yandex.cloud.api.ai.stt.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/stt/v3;stt'
  _CODETYPE.values_by_name["CODE_TYPE_UNSPECIFIED"]._options = None
  _CODETYPE.values_by_name["CODE_TYPE_UNSPECIFIED"]._serialized_options = b'\010\001'
  _RECOGNITIONCLASSIFIER_TRIGGERTYPE.values_by_name["TRIGGER_TYPE_UNSPECIFIED"]._options = None
  _RECOGNITIONCLASSIFIER_TRIGGERTYPE.values_by_name["TRIGGER_TYPE_UNSPECIFIED"]._serialized_options = b'\010\001'
  _ALTERNATIVEUPDATE.fields_by_name['channel_tag']._options = None
  _ALTERNATIVEUPDATE.fields_by_name['channel_tag']._serialized_options = b'\030\001'
  _RECOGNITIONCLASSIFIERUPDATE_WINDOWTYPE.values_by_name["WINDOW_TYPE_UNSPECIFIED"]._options = None
  _RECOGNITIONCLASSIFIERUPDATE_WINDOWTYPE.values_by_name["WINDOW_TYPE_UNSPECIFIED"]._serialized_options = b'\010\001'
  _SPEAKERANALYSIS_WINDOWTYPE.values_by_name["WINDOW_TYPE_UNSPECIFIED"]._options = None
  _SPEAKERANALYSIS_WINDOWTYPE.values_by_name["WINDOW_TYPE_UNSPECIFIED"]._serialized_options = b'\010\001'
  _globals['_CODETYPE']._serialized_start=7877
  _globals['_CODETYPE']._serialized_end=7956
  _globals['_TEXTNORMALIZATIONOPTIONS']._serialized_start=55
  _globals['_TEXTNORMALIZATIONOPTIONS']._serialized_end=537
  _globals['_TEXTNORMALIZATIONOPTIONS_TEXTNORMALIZATION']._serialized_start=319
  _globals['_TEXTNORMALIZATIONOPTIONS_TEXTNORMALIZATION']._serialized_end=439
  _globals['_TEXTNORMALIZATIONOPTIONS_PHONEFORMATTINGMODE']._serialized_start=441
  _globals['_TEXTNORMALIZATIONOPTIONS_PHONEFORMATTINGMODE']._serialized_end=537
  _globals['_DEFAULTEOUCLASSIFIER']._serialized_start=540
  _globals['_DEFAULTEOUCLASSIFIER']._serialized_end=746
  _globals['_DEFAULTEOUCLASSIFIER_EOUSENSITIVITY']._serialized_start=674
  _globals['_DEFAULTEOUCLASSIFIER_EOUSENSITIVITY']._serialized_end=746
  _globals['_EXTERNALEOUCLASSIFIER']._serialized_start=748
  _globals['_EXTERNALEOUCLASSIFIER']._serialized_end=771
  _globals['_EOUCLASSIFIEROPTIONS']._serialized_start=774
  _globals['_EOUCLASSIFIEROPTIONS']._serialized_end=952
  _globals['_RECOGNITIONCLASSIFIER']._serialized_start=955
  _globals['_RECOGNITIONCLASSIFIER']._serialized_end=1166
  _globals['_RECOGNITIONCLASSIFIER_TRIGGERTYPE']._serialized_start=1071
  _globals['_RECOGNITIONCLASSIFIER_TRIGGERTYPE']._serialized_end=1166
  _globals['_RECOGNITIONCLASSIFIEROPTIONS']._serialized_start=1168
  _globals['_RECOGNITIONCLASSIFIEROPTIONS']._serialized_end=1260
  _globals['_SPEECHANALYSISOPTIONS']._serialized_start=1263
  _globals['_SPEECHANALYSISOPTIONS']._serialized_end=1399
  _globals['_RAWAUDIO']._serialized_start=1402
  _globals['_RAWAUDIO']._serialized_end=1601
  _globals['_RAWAUDIO_AUDIOENCODING']._serialized_start=1536
  _globals['_RAWAUDIO_AUDIOENCODING']._serialized_end=1601
  _globals['_CONTAINERAUDIO']._serialized_start=1604
  _globals['_CONTAINERAUDIO']._serialized_end=1795
  _globals['_CONTAINERAUDIO_CONTAINERAUDIOTYPE']._serialized_start=1705
  _globals['_CONTAINERAUDIO_CONTAINERAUDIOTYPE']._serialized_end=1795
  _globals['_AUDIOFORMATOPTIONS']._serialized_start=1798
  _globals['_AUDIOFORMATOPTIONS']._serialized_end=1943
  _globals['_LANGUAGERESTRICTIONOPTIONS']._serialized_start=1946
  _globals['_LANGUAGERESTRICTIONOPTIONS']._serialized_end=2193
  _globals['_LANGUAGERESTRICTIONOPTIONS_LANGUAGERESTRICTIONTYPE']._serialized_start=2095
  _globals['_LANGUAGERESTRICTIONOPTIONS_LANGUAGERESTRICTIONTYPE']._serialized_end=2193
  _globals['_RECOGNITIONMODELOPTIONS']._serialized_start=2196
  _globals['_RECOGNITIONMODELOPTIONS']._serialized_end=2630
  _globals['_RECOGNITIONMODELOPTIONS_AUDIOPROCESSINGTYPE']._serialized_start=2540
  _globals['_RECOGNITIONMODELOPTIONS_AUDIOPROCESSINGTYPE']._serialized_end=2630
  _globals['_SPEAKERLABELINGOPTIONS']._serialized_start=2633
  _globals['_SPEAKERLABELINGOPTIONS']._serialized_end=2855
  _globals['_SPEAKERLABELINGOPTIONS_SPEAKERLABELING']._serialized_start=2743
  _globals['_SPEAKERLABELINGOPTIONS_SPEAKERLABELING']._serialized_end=2855
  _globals['_STREAMINGOPTIONS']._serialized_start=2858
  _globals['_STREAMINGOPTIONS']._serialized_end=3224
  _globals['_AUDIOCHUNK']._serialized_start=3226
  _globals['_AUDIOCHUNK']._serialized_end=3252
  _globals['_SILENCECHUNK']._serialized_start=3254
  _globals['_SILENCECHUNK']._serialized_end=3289
  _globals['_EOU']._serialized_start=3291
  _globals['_EOU']._serialized_end=3296
  _globals['_STREAMINGREQUEST']._serialized_start=3299
  _globals['_STREAMINGREQUEST']._serialized_end=3531
  _globals['_RECOGNIZEFILEREQUEST']._serialized_start=3534
  _globals['_RECOGNIZEFILEREQUEST']._serialized_end=3889
  _globals['_WORD']._serialized_start=3891
  _globals['_WORD']._serialized_end=3955
  _globals['_LANGUAGEESTIMATION']._serialized_start=3957
  _globals['_LANGUAGEESTIMATION']._serialized_end=4021
  _globals['_ALTERNATIVE']._serialized_start=4024
  _globals['_ALTERNATIVE']._serialized_end=4211
  _globals['_EOUUPDATE']._serialized_start=4213
  _globals['_EOUUPDATE']._serialized_end=4241
  _globals['_ALTERNATIVEUPDATE']._serialized_start=4243
  _globals['_ALTERNATIVEUPDATE']._serialized_end=4340
  _globals['_AUDIOCURSORS']._serialized_start=4343
  _globals['_AUDIOCURSORS']._serialized_end=4496
  _globals['_FINALREFINEMENT']._serialized_start=4498
  _globals['_FINALREFINEMENT']._serialized_end=4608
  _globals['_STATUSCODE']._serialized_start=4610
  _globals['_STATUSCODE']._serialized_end=4686
  _globals['_SESSIONUUID']._serialized_start=4688
  _globals['_SESSIONUUID']._serialized_end=4740
  _globals['_PHRASEHIGHLIGHT']._serialized_start=4742
  _globals['_PHRASEHIGHLIGHT']._serialized_end=4817
  _globals['_RECOGNITIONCLASSIFIERLABEL']._serialized_start=4819
  _globals['_RECOGNITIONCLASSIFIERLABEL']._serialized_end=4882
  _globals['_RECOGNITIONCLASSIFIERRESULT']._serialized_start=4885
  _globals['_RECOGNITIONCLASSIFIERRESULT']._serialized_end=5051
  _globals['_RECOGNITIONCLASSIFIERUPDATE']._serialized_start=5054
  _globals['_RECOGNITIONCLASSIFIERUPDATE']._serialized_end=5381
  _globals['_RECOGNITIONCLASSIFIERUPDATE_WINDOWTYPE']._serialized_start=5282
  _globals['_RECOGNITIONCLASSIFIERUPDATE_WINDOWTYPE']._serialized_end=5381
  _globals['_DESCRIPTIVESTATISTICS']._serialized_start=5384
  _globals['_DESCRIPTIVESTATISTICS']._serialized_end=5571
  _globals['_DESCRIPTIVESTATISTICS_QUANTILE']._serialized_start=5531
  _globals['_DESCRIPTIVESTATISTICS_QUANTILE']._serialized_end=5571
  _globals['_AUDIOSEGMENTBOUNDARIES']._serialized_start=5573
  _globals['_AUDIOSEGMENTBOUNDARIES']._serialized_end=5641
  _globals['_SPEAKERANALYSIS']._serialized_start=5644
  _globals['_SPEAKERANALYSIS']._serialized_end=6419
  _globals['_SPEAKERANALYSIS_WINDOWTYPE']._serialized_start=6343
  _globals['_SPEAKERANALYSIS_WINDOWTYPE']._serialized_end=6419
  _globals['_CONVERSATIONANALYSIS']._serialized_start=6422
  _globals['_CONVERSATIONANALYSIS']._serialized_end=7195
  _globals['_CONVERSATIONANALYSIS_INTERRUPTSEVALUATION']._serialized_start=7032
  _globals['_CONVERSATIONANALYSIS_INTERRUPTSEVALUATION']._serialized_end=7195
  _globals['_STREAMINGRESPONSE']._serialized_start=7198
  _globals['_STREAMINGRESPONSE']._serialized_end=7875
# @@protoc_insertion_point(module_scope)
