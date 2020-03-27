# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/losses.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/losses.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n$object_detection/protos/losses.proto\x12\x17object_detection.protos\"\xfe\x05\n\x04Loss\x12\x44\n\x11localization_loss\x18\x01 \x01(\x0b\x32).object_detection.protos.LocalizationLoss\x12H\n\x13\x63lassification_loss\x18\x02 \x01(\x0b\x32+.object_detection.protos.ClassificationLoss\x12\x45\n\x12hard_example_miner\x18\x03 \x01(\x0b\x32).object_detection.protos.HardExampleMiner\x12 \n\x15\x63lassification_weight\x18\x04 \x01(\x02:\x01\x31\x12\x1e\n\x13localization_weight\x18\x05 \x01(\x02:\x01\x31\x12M\n\x16random_example_sampler\x18\x06 \x01(\x0b\x32-.object_detection.protos.RandomExampleSampler\x12I\n\x11\x65qualization_loss\x18\x07 \x01(\x0b\x32..object_detection.protos.Loss.EqualizationLoss\x12V\n\x15\x65xpected_loss_weights\x18\x12 \x01(\x0e\x32\x31.object_detection.protos.Loss.ExpectedLossWeights:\x04NONE\x12#\n\x18min_num_negative_samples\x18\x13 \x01(\x02:\x01\x30\x12*\n\x1f\x64\x65sired_negative_sampling_ratio\x18\x14 \x01(\x02:\x01\x33\x1a?\n\x10\x45qualizationLoss\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x30\x12\x18\n\x10\x65xclude_prefixes\x18\x02 \x03(\t\"Y\n\x13\x45xpectedLossWeights\x12\x08\n\x04NONE\x10\x00\x12\x15\n\x11\x45XPECTED_SAMPLING\x10\x01\x12!\n\x1dREWEIGHTING_UNMATCHED_ANCHORS\x10\x02\"\x9a\x02\n\x10LocalizationLoss\x12J\n\x0bweighted_l2\x18\x01 \x01(\x0b\x32\x33.object_detection.protos.WeightedL2LocalizationLossH\x00\x12W\n\x12weighted_smooth_l1\x18\x02 \x01(\x0b\x32\x39.object_detection.protos.WeightedSmoothL1LocalizationLossH\x00\x12L\n\x0cweighted_iou\x18\x03 \x01(\x0b\x32\x34.object_detection.protos.WeightedIOULocalizationLossH\x00\x42\x13\n\x11localization_loss\">\n\x1aWeightedL2LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"V\n WeightedSmoothL1LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05\x64\x65lta\x18\x02 \x01(\x02:\x01\x31\"\x1d\n\x1bWeightedIOULocalizationLoss\"\x82\x04\n\x12\x43lassificationLoss\x12V\n\x10weighted_sigmoid\x18\x01 \x01(\x0b\x32:.object_detection.protos.WeightedSigmoidClassificationLossH\x00\x12V\n\x10weighted_softmax\x18\x02 \x01(\x0b\x32:.object_detection.protos.WeightedSoftmaxClassificationLossH\x00\x12j\n\x17weighted_logits_softmax\x18\x05 \x01(\x0b\x32G.object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLossH\x00\x12^\n\x14\x62ootstrapped_sigmoid\x18\x03 \x01(\x0b\x32>.object_detection.protos.BootstrappedSigmoidClassificationLossH\x00\x12Y\n\x16weighted_sigmoid_focal\x18\x04 \x01(\x0b\x32\x37.object_detection.protos.SigmoidFocalClassificationLossH\x00\x42\x15\n\x13\x63lassification_loss\"E\n!WeightedSigmoidClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"c\n\x1eSigmoidFocalClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05gamma\x18\x02 \x01(\x02:\x01\x32\x12\r\n\x05\x61lpha\x18\x03 \x01(\x02\"]\n!WeightedSoftmaxClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0blogit_scale\x18\x02 \x01(\x02:\x01\x31\"j\n.WeightedSoftmaxClassificationAgainstLogitsLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0blogit_scale\x18\x02 \x01(\x02:\x01\x31\"w\n%BootstrappedSigmoidClassificationLoss\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12\x1d\n\x0ehard_bootstrap\x18\x02 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x61nchorwise_output\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xa1\x02\n\x10HardExampleMiner\x12\x1d\n\x11num_hard_examples\x18\x01 \x01(\x05:\x02\x36\x34\x12\x1a\n\riou_threshold\x18\x02 \x01(\x02:\x03\x30.7\x12K\n\tloss_type\x18\x03 \x01(\x0e\x32\x32.object_detection.protos.HardExampleMiner.LossType:\x04\x42OTH\x12%\n\x1amax_negatives_per_positive\x18\x04 \x01(\x05:\x01\x30\x12\"\n\x17min_negatives_per_image\x18\x05 \x01(\x05:\x01\x30\":\n\x08LossType\x12\x08\n\x04\x42OTH\x10\x00\x12\x12\n\x0e\x43LASSIFICATION\x10\x01\x12\x10\n\x0cLOCALIZATION\x10\x02\">\n\x14RandomExampleSampler\x12&\n\x18positive_sample_fraction\x18\x01 \x01(\x02:\x04\x30.01'
)



_LOSS_EXPECTEDLOSSWEIGHTS = _descriptor.EnumDescriptor(
  name='ExpectedLossWeights',
  full_name='object_detection.protos.Loss.ExpectedLossWeights',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_SAMPLING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REWEIGHTING_UNMATCHED_ANCHORS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=743,
  serialized_end=832,
)
_sym_db.RegisterEnumDescriptor(_LOSS_EXPECTEDLOSSWEIGHTS)

_HARDEXAMPLEMINER_LOSSTYPE = _descriptor.EnumDescriptor(
  name='LossType',
  full_name='object_detection.protos.HardExampleMiner.LossType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASSIFICATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCALIZATION', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2547,
  serialized_end=2605,
)
_sym_db.RegisterEnumDescriptor(_HARDEXAMPLEMINER_LOSSTYPE)


_LOSS_EQUALIZATIONLOSS = _descriptor.Descriptor(
  name='EqualizationLoss',
  full_name='object_detection.protos.Loss.EqualizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='object_detection.protos.Loss.EqualizationLoss.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclude_prefixes', full_name='object_detection.protos.Loss.EqualizationLoss.exclude_prefixes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=678,
  serialized_end=741,
)

_LOSS = _descriptor.Descriptor(
  name='Loss',
  full_name='object_detection.protos.Loss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='localization_loss', full_name='object_detection.protos.Loss.localization_loss', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_loss', full_name='object_detection.protos.Loss.classification_loss', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hard_example_miner', full_name='object_detection.protos.Loss.hard_example_miner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_weight', full_name='object_detection.protos.Loss.classification_weight', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localization_weight', full_name='object_detection.protos.Loss.localization_weight', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_example_sampler', full_name='object_detection.protos.Loss.random_example_sampler', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equalization_loss', full_name='object_detection.protos.Loss.equalization_loss', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_loss_weights', full_name='object_detection.protos.Loss.expected_loss_weights', index=7,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_num_negative_samples', full_name='object_detection.protos.Loss.min_num_negative_samples', index=8,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desired_negative_sampling_ratio', full_name='object_detection.protos.Loss.desired_negative_sampling_ratio', index=9,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOSS_EQUALIZATIONLOSS, ],
  enum_types=[
    _LOSS_EXPECTEDLOSSWEIGHTS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=832,
)


_LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='LocalizationLoss',
  full_name='object_detection.protos.LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weighted_l2', full_name='object_detection.protos.LocalizationLoss.weighted_l2', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted_smooth_l1', full_name='object_detection.protos.LocalizationLoss.weighted_smooth_l1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted_iou', full_name='object_detection.protos.LocalizationLoss.weighted_iou', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='localization_loss', full_name='object_detection.protos.LocalizationLoss.localization_loss',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=835,
  serialized_end=1117,
)


_WEIGHTEDL2LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedL2LocalizationLoss',
  full_name='object_detection.protos.WeightedL2LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.WeightedL2LocalizationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1119,
  serialized_end=1181,
)


_WEIGHTEDSMOOTHL1LOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedSmoothL1LocalizationLoss',
  full_name='object_detection.protos.WeightedSmoothL1LocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.WeightedSmoothL1LocalizationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delta', full_name='object_detection.protos.WeightedSmoothL1LocalizationLoss.delta', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1183,
  serialized_end=1269,
)


_WEIGHTEDIOULOCALIZATIONLOSS = _descriptor.Descriptor(
  name='WeightedIOULocalizationLoss',
  full_name='object_detection.protos.WeightedIOULocalizationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1271,
  serialized_end=1300,
)


_CLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='ClassificationLoss',
  full_name='object_detection.protos.ClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weighted_sigmoid', full_name='object_detection.protos.ClassificationLoss.weighted_sigmoid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted_softmax', full_name='object_detection.protos.ClassificationLoss.weighted_softmax', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted_logits_softmax', full_name='object_detection.protos.ClassificationLoss.weighted_logits_softmax', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bootstrapped_sigmoid', full_name='object_detection.protos.ClassificationLoss.bootstrapped_sigmoid', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted_sigmoid_focal', full_name='object_detection.protos.ClassificationLoss.weighted_sigmoid_focal', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='classification_loss', full_name='object_detection.protos.ClassificationLoss.classification_loss',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1303,
  serialized_end=1817,
)


_WEIGHTEDSIGMOIDCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='WeightedSigmoidClassificationLoss',
  full_name='object_detection.protos.WeightedSigmoidClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.WeightedSigmoidClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1819,
  serialized_end=1888,
)


_SIGMOIDFOCALCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='SigmoidFocalClassificationLoss',
  full_name='object_detection.protos.SigmoidFocalClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.SigmoidFocalClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='object_detection.protos.SigmoidFocalClassificationLoss.gamma', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='object_detection.protos.SigmoidFocalClassificationLoss.alpha', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1890,
  serialized_end=1989,
)


_WEIGHTEDSOFTMAXCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='WeightedSoftmaxClassificationLoss',
  full_name='object_detection.protos.WeightedSoftmaxClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.WeightedSoftmaxClassificationLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logit_scale', full_name='object_detection.protos.WeightedSoftmaxClassificationLoss.logit_scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1991,
  serialized_end=2084,
)


_WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS = _descriptor.Descriptor(
  name='WeightedSoftmaxClassificationAgainstLogitsLoss',
  full_name='object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLoss.anchorwise_output', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logit_scale', full_name='object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLoss.logit_scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2086,
  serialized_end=2192,
)


_BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='BootstrappedSigmoidClassificationLoss',
  full_name='object_detection.protos.BootstrappedSigmoidClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha', full_name='object_detection.protos.BootstrappedSigmoidClassificationLoss.alpha', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hard_bootstrap', full_name='object_detection.protos.BootstrappedSigmoidClassificationLoss.hard_bootstrap', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='anchorwise_output', full_name='object_detection.protos.BootstrappedSigmoidClassificationLoss.anchorwise_output', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2194,
  serialized_end=2313,
)


_HARDEXAMPLEMINER = _descriptor.Descriptor(
  name='HardExampleMiner',
  full_name='object_detection.protos.HardExampleMiner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_hard_examples', full_name='object_detection.protos.HardExampleMiner.num_hard_examples', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iou_threshold', full_name='object_detection.protos.HardExampleMiner.iou_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.7),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_type', full_name='object_detection.protos.HardExampleMiner.loss_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_negatives_per_positive', full_name='object_detection.protos.HardExampleMiner.max_negatives_per_positive', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_negatives_per_image', full_name='object_detection.protos.HardExampleMiner.min_negatives_per_image', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HARDEXAMPLEMINER_LOSSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2316,
  serialized_end=2605,
)


_RANDOMEXAMPLESAMPLER = _descriptor.Descriptor(
  name='RandomExampleSampler',
  full_name='object_detection.protos.RandomExampleSampler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='positive_sample_fraction', full_name='object_detection.protos.RandomExampleSampler.positive_sample_fraction', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2607,
  serialized_end=2669,
)

_LOSS_EQUALIZATIONLOSS.containing_type = _LOSS
_LOSS.fields_by_name['localization_loss'].message_type = _LOCALIZATIONLOSS
_LOSS.fields_by_name['classification_loss'].message_type = _CLASSIFICATIONLOSS
_LOSS.fields_by_name['hard_example_miner'].message_type = _HARDEXAMPLEMINER
_LOSS.fields_by_name['random_example_sampler'].message_type = _RANDOMEXAMPLESAMPLER
_LOSS.fields_by_name['equalization_loss'].message_type = _LOSS_EQUALIZATIONLOSS
_LOSS.fields_by_name['expected_loss_weights'].enum_type = _LOSS_EXPECTEDLOSSWEIGHTS
_LOSS_EXPECTEDLOSSWEIGHTS.containing_type = _LOSS
_LOCALIZATIONLOSS.fields_by_name['weighted_l2'].message_type = _WEIGHTEDL2LOCALIZATIONLOSS
_LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'].message_type = _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS
_LOCALIZATIONLOSS.fields_by_name['weighted_iou'].message_type = _WEIGHTEDIOULOCALIZATIONLOSS
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_l2'])
_LOCALIZATIONLOSS.fields_by_name['weighted_l2'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'])
_LOCALIZATIONLOSS.fields_by_name['weighted_smooth_l1'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_LOCALIZATIONLOSS.oneofs_by_name['localization_loss'].fields.append(
  _LOCALIZATIONLOSS.fields_by_name['weighted_iou'])
_LOCALIZATIONLOSS.fields_by_name['weighted_iou'].containing_oneof = _LOCALIZATIONLOSS.oneofs_by_name['localization_loss']
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'].message_type = _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'].message_type = _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['weighted_logits_softmax'].message_type = _WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS
_CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'].message_type = _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'].message_type = _SIGMOIDFOCALCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_softmax'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_logits_softmax'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_logits_softmax'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'])
_CLASSIFICATIONLOSS.fields_by_name['bootstrapped_sigmoid'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_CLASSIFICATIONLOSS.oneofs_by_name['classification_loss'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'])
_CLASSIFICATIONLOSS.fields_by_name['weighted_sigmoid_focal'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['classification_loss']
_HARDEXAMPLEMINER.fields_by_name['loss_type'].enum_type = _HARDEXAMPLEMINER_LOSSTYPE
_HARDEXAMPLEMINER_LOSSTYPE.containing_type = _HARDEXAMPLEMINER
DESCRIPTOR.message_types_by_name['Loss'] = _LOSS
DESCRIPTOR.message_types_by_name['LocalizationLoss'] = _LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedL2LocalizationLoss'] = _WEIGHTEDL2LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSmoothL1LocalizationLoss'] = _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedIOULocalizationLoss'] = _WEIGHTEDIOULOCALIZATIONLOSS
DESCRIPTOR.message_types_by_name['ClassificationLoss'] = _CLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSigmoidClassificationLoss'] = _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['SigmoidFocalClassificationLoss'] = _SIGMOIDFOCALCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSoftmaxClassificationLoss'] = _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['WeightedSoftmaxClassificationAgainstLogitsLoss'] = _WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS
DESCRIPTOR.message_types_by_name['BootstrappedSigmoidClassificationLoss'] = _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['HardExampleMiner'] = _HARDEXAMPLEMINER
DESCRIPTOR.message_types_by_name['RandomExampleSampler'] = _RANDOMEXAMPLESAMPLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Loss = _reflection.GeneratedProtocolMessageType('Loss', (_message.Message,), {

  'EqualizationLoss' : _reflection.GeneratedProtocolMessageType('EqualizationLoss', (_message.Message,), {
    'DESCRIPTOR' : _LOSS_EQUALIZATIONLOSS,
    '__module__' : 'object_detection.protos.losses_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.Loss.EqualizationLoss)
    })
  ,
  'DESCRIPTOR' : _LOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Loss)
  })
_sym_db.RegisterMessage(Loss)
_sym_db.RegisterMessage(Loss.EqualizationLoss)

LocalizationLoss = _reflection.GeneratedProtocolMessageType('LocalizationLoss', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.LocalizationLoss)
  })
_sym_db.RegisterMessage(LocalizationLoss)

WeightedL2LocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedL2LocalizationLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDL2LOCALIZATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedL2LocalizationLoss)
  })
_sym_db.RegisterMessage(WeightedL2LocalizationLoss)

WeightedSmoothL1LocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedSmoothL1LocalizationLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDSMOOTHL1LOCALIZATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedSmoothL1LocalizationLoss)
  })
_sym_db.RegisterMessage(WeightedSmoothL1LocalizationLoss)

WeightedIOULocalizationLoss = _reflection.GeneratedProtocolMessageType('WeightedIOULocalizationLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDIOULOCALIZATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedIOULocalizationLoss)
  })
_sym_db.RegisterMessage(WeightedIOULocalizationLoss)

ClassificationLoss = _reflection.GeneratedProtocolMessageType('ClassificationLoss', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ClassificationLoss)
  })
_sym_db.RegisterMessage(ClassificationLoss)

WeightedSigmoidClassificationLoss = _reflection.GeneratedProtocolMessageType('WeightedSigmoidClassificationLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDSIGMOIDCLASSIFICATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedSigmoidClassificationLoss)
  })
_sym_db.RegisterMessage(WeightedSigmoidClassificationLoss)

SigmoidFocalClassificationLoss = _reflection.GeneratedProtocolMessageType('SigmoidFocalClassificationLoss', (_message.Message,), {
  'DESCRIPTOR' : _SIGMOIDFOCALCLASSIFICATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SigmoidFocalClassificationLoss)
  })
_sym_db.RegisterMessage(SigmoidFocalClassificationLoss)

WeightedSoftmaxClassificationLoss = _reflection.GeneratedProtocolMessageType('WeightedSoftmaxClassificationLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDSOFTMAXCLASSIFICATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedSoftmaxClassificationLoss)
  })
_sym_db.RegisterMessage(WeightedSoftmaxClassificationLoss)

WeightedSoftmaxClassificationAgainstLogitsLoss = _reflection.GeneratedProtocolMessageType('WeightedSoftmaxClassificationAgainstLogitsLoss', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLoss)
  })
_sym_db.RegisterMessage(WeightedSoftmaxClassificationAgainstLogitsLoss)

BootstrappedSigmoidClassificationLoss = _reflection.GeneratedProtocolMessageType('BootstrappedSigmoidClassificationLoss', (_message.Message,), {
  'DESCRIPTOR' : _BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.BootstrappedSigmoidClassificationLoss)
  })
_sym_db.RegisterMessage(BootstrappedSigmoidClassificationLoss)

HardExampleMiner = _reflection.GeneratedProtocolMessageType('HardExampleMiner', (_message.Message,), {
  'DESCRIPTOR' : _HARDEXAMPLEMINER,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.HardExampleMiner)
  })
_sym_db.RegisterMessage(HardExampleMiner)

RandomExampleSampler = _reflection.GeneratedProtocolMessageType('RandomExampleSampler', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMEXAMPLESAMPLER,
  '__module__' : 'object_detection.protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomExampleSampler)
  })
_sym_db.RegisterMessage(RandomExampleSampler)


# @@protoc_insertion_point(module_scope)
