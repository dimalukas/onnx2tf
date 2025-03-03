# onnx2tf
Self-Created Tools to convert ONNX files (NCHW) to TensorFlow/TFLite/Keras format (NHWC). The purpose of this tool is to solve the massive Transpose extrapolation problem in [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow) ([onnx-tf](https://pypi.org/project/onnx-tf/)). I don't need a Star, but give me a pull request. Since I am adding challenging model optimizations and fixing bugs almost daily, I frequently embed potential bugs that would otherwise break through CI's regression testing. Therefore, if you encounter new problems, I recommend that you try a package that is a few versions older, or try the latest package that will be released in a few days.

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/193840307-fa69eace-05a9-4d93-9c5d-999cf88af28e.png" />
</p>

[![Downloads](https://static.pepy.tech/personalized-badge/onnx2tf?period=total&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/onnx2tf) ![GitHub](https://img.shields.io/github/license/PINTO0309/onnx2tf?color=2BAF2B) [![Python](https://img.shields.io/badge/Python-3.8-2BAF2B)](https://img.shields.io/badge/Python-3.8-2BAF2B) [![PyPI](https://img.shields.io/pypi/v/onnx2tf?color=2BAF2B)](https://pypi.org/project/onnx2tf/) [![CodeQL](https://github.com/PINTO0309/onnx2tf/workflows/CodeQL/badge.svg)](https://github.com/PINTO0309/onnx2tf/actions?query=workflow%3ACodeQL) ![Model Convert Test Status](https://github.com/PINTO0309/onnx2tf/workflows/Model%20Convert%20Test/badge.svg) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7230085.svg)](https://doi.org/10.5281/zenodo.7230085)

## Model Conversion Status
https://github.com/PINTO0309/onnx2tf/wiki/model_status

## Supported layers
- https://github.com/onnx/onnx/blob/main/docs/Operators.md
- :heavy_check_mark:: Supported　:white_check_mark:: Partial support　**Help wanted**: Pull Request are welcome

  <details><summary>See the list of supported layers</summary><div>

  |OP|Status|
  |:-|:-:|
  |Abs|:heavy_check_mark:|
  |Acosh|:heavy_check_mark:|
  |Acos|:heavy_check_mark:|
  |Add|:heavy_check_mark:|
  |And|:heavy_check_mark:|
  |ArgMax|:heavy_check_mark:|
  |ArgMin|:heavy_check_mark:|
  |Asinh|:heavy_check_mark:|
  |Asin|:heavy_check_mark:|
  |Atanh|:heavy_check_mark:|
  |Atan|:heavy_check_mark:|
  |AveragePool|:heavy_check_mark:|
  |BatchNormalization|:heavy_check_mark:|
  |Bernoulli|:heavy_check_mark:|
  |BitShift|:heavy_check_mark:|
  |BitwiseAnd|**Help wanted**|
  |BitwiseNot|**Help wanted**|
  |BitwiseOr|**Help wanted**|
  |BitwiseXor|**Help wanted**|
  |Cast|:heavy_check_mark:|
  |Ceil|:heavy_check_mark:|
  |Celu|:heavy_check_mark:|
  |CenterCropPad|**Help wanted**|
  |Clip|:heavy_check_mark:|
  |Col2Im|**Help wanted**|
  |Compress|:heavy_check_mark:|
  |ConcatFromSequence|:heavy_check_mark:|
  |Concat|:heavy_check_mark:|
  |ConstantOfShape|:heavy_check_mark:|
  |Constant|:heavy_check_mark:|
  |Conv|:heavy_check_mark:|
  |ConvTranspose|:heavy_check_mark:|
  |Cosh|:heavy_check_mark:|
  |Cos|:heavy_check_mark:|
  |CumSum|:heavy_check_mark:|
  |DeformConv|**Help wanted**|
  |DepthToSpace|:heavy_check_mark:|
  |Det|:heavy_check_mark:|
  |DequantizeLinear|:heavy_check_mark:|
  |DFT|**Help wanted**|
  |Div|:heavy_check_mark:|
  |Dropout|:heavy_check_mark:|
  |DynamicQuantizeLinear|:heavy_check_mark:|
  |Einsum|:heavy_check_mark:|
  |Elu|:heavy_check_mark:|
  |Equal|:heavy_check_mark:|
  |Erf|:heavy_check_mark:|
  |Expand|:heavy_check_mark:|
  |Exp|:heavy_check_mark:|
  |EyeLike|:heavy_check_mark:|
  |Flatten|:heavy_check_mark:|
  |Floor|:heavy_check_mark:|
  |FusedConv|:heavy_check_mark:|
  |GatherElements|:heavy_check_mark:|
  |GatherND|:heavy_check_mark:|
  |Gather|:heavy_check_mark:|
  |Gemm|:heavy_check_mark:|
  |GlobalAveragePool|:heavy_check_mark:|
  |GlobalLpPool|:heavy_check_mark:|
  |GlobalMaxPool|:heavy_check_mark:|
  |GreaterOrEqual|:heavy_check_mark:|
  |Greater|:heavy_check_mark:|
  |GridSample|:white_check_mark:|
  |GroupNormalization|**Help wanted**|
  |GRU|:heavy_check_mark:|
  |HammingWindow|:white_check_mark:|
  |HannWindow|:white_check_mark:|
  |Hardmax|:heavy_check_mark:|
  |HardSigmoid|:heavy_check_mark:|
  |HardSwish|:heavy_check_mark:|
  |Identity|:heavy_check_mark:|
  |If|:heavy_check_mark:|
  |Input|:heavy_check_mark:|
  |InstanceNormalization|:heavy_check_mark:|
  |Inverse|:heavy_check_mark:|
  |IsInf|:heavy_check_mark:|
  |IsNaN|:heavy_check_mark:|
  |LayerNormalization|:heavy_check_mark:|
  |LeakyRelu|:heavy_check_mark:|
  |LessOrEqual|:heavy_check_mark:|
  |Less|:heavy_check_mark:|
  |Log|:heavy_check_mark:|
  |LogSoftmax|:heavy_check_mark:|
  |Loop|**Help wanted**|
  |LpNormalization|:heavy_check_mark:|
  |LRN|:heavy_check_mark:|
  |LSTM|:heavy_check_mark:|
  |MatMul|:heavy_check_mark:|
  |MatMulInteger|:heavy_check_mark:|
  |MaxPool|:heavy_check_mark:|
  |Max|:heavy_check_mark:|
  |MaxRoiPool|**Help wanted**|
  |MaxUnpool|:heavy_check_mark:|
  |Mean|:heavy_check_mark:|
  |MeanVarianceNormalization|:heavy_check_mark:|
  |MelWeightMatrix|:heavy_check_mark:|
  |Min|:heavy_check_mark:|
  |Mish|:heavy_check_mark:|
  |Mod|:heavy_check_mark:|
  |Mul|:heavy_check_mark:|
  |Multinomial|:heavy_check_mark:|
  |Neg|:heavy_check_mark:|
  |NonMaxSuppression|:heavy_check_mark:|
  |NonZero|:heavy_check_mark:|
  |Optional|**Help wanted**|
  |OptionalGetElement|:heavy_check_mark:|
  |OptionalHasElement|:heavy_check_mark:|
  |Not|:heavy_check_mark:|
  |OneHot|:heavy_check_mark:|
  |Or|:heavy_check_mark:|
  |Pad|:heavy_check_mark:|
  |Pow|:heavy_check_mark:|
  |PRelu|:heavy_check_mark:|
  |QLinearAdd|:heavy_check_mark:|
  |QLinearConcat|:heavy_check_mark:|
  |QLinearConv|:heavy_check_mark:|
  |QLinearLeakyRelu|:heavy_check_mark:|
  |QLinearMatMul|:heavy_check_mark:|
  |QLinearMul|:heavy_check_mark:|
  |QLinearSigmoid|:heavy_check_mark:|
  |QLinearSoftmax|:heavy_check_mark:|
  |QuantizeLinear|:heavy_check_mark:|
  |RandomNormalLike|:heavy_check_mark:|
  |RandomNormal|:heavy_check_mark:|
  |RandomUniformLike|:heavy_check_mark:|
  |RandomUniform|:heavy_check_mark:|
  |Range|:heavy_check_mark:|
  |Reciprocal|:heavy_check_mark:|
  |ReduceL1|:heavy_check_mark:|
  |ReduceL2|:heavy_check_mark:|
  |ReduceLogSum|:heavy_check_mark:|
  |ReduceLogSumExp|:heavy_check_mark:|
  |ReduceMax|:heavy_check_mark:|
  |ReduceMean|:heavy_check_mark:|
  |ReduceMin|:heavy_check_mark:|
  |ReduceProd|:heavy_check_mark:|
  |ReduceSum|:heavy_check_mark:|
  |ReduceSumSquare|:heavy_check_mark:|
  |Relu|:heavy_check_mark:|
  |Reshape|:heavy_check_mark:|
  |Resize|:heavy_check_mark:|
  |ReverseSequence|:heavy_check_mark:|
  |RNN|:heavy_check_mark:|
  |RoiAlign|:heavy_check_mark:|
  |Round|:heavy_check_mark:|
  |ScaleAndTranslate|:heavy_check_mark:|
  |Scatter|:heavy_check_mark:|
  |ScatterElements|:heavy_check_mark:|
  |ScatterND|:heavy_check_mark:|
  |Scan|**Help wanted**|
  |Selu|:heavy_check_mark:|
  |SequenceAt|:heavy_check_mark:|
  |SequenceConstruct|:heavy_check_mark:|
  |SequenceEmpty|:heavy_check_mark:|
  |SequenceErase|:heavy_check_mark:|
  |SequenceInsert|:heavy_check_mark:|
  |SequenceLength|:heavy_check_mark:|
  |Shape|:heavy_check_mark:|
  |Shrink|:heavy_check_mark:|
  |Sigmoid|:heavy_check_mark:|
  |Sign|:heavy_check_mark:|
  |Sinh|:heavy_check_mark:|
  |Sin|:heavy_check_mark:|
  |Size|:heavy_check_mark:|
  |Slice|:heavy_check_mark:|
  |Softmax|:heavy_check_mark:|
  |Softplus|:heavy_check_mark:|
  |Softsign|:heavy_check_mark:|
  |SpaceToDepth|:heavy_check_mark:|
  |Split|:heavy_check_mark:|
  |SplitToSequence|:heavy_check_mark:|
  |Sqrt|:heavy_check_mark:|
  |Squeeze|:heavy_check_mark:|
  |STFT|**Help wanted**|
  |StringNormalizer|:white_check_mark:|
  |Sub|:heavy_check_mark:|
  |Sum|:heavy_check_mark:|
  |Tanh|:heavy_check_mark:|
  |Tan|:heavy_check_mark:|
  |TfIdfVectorizer|**Help wanted**|
  |ThresholdedRelu|:heavy_check_mark:|
  |Tile|:heavy_check_mark:|
  |TopK|:heavy_check_mark:|
  |Transpose|:heavy_check_mark:|
  |Trilu|:heavy_check_mark:|
  |Unique|:heavy_check_mark:|
  |Unsqueeze|:heavy_check_mark:|
  |Upsample|:heavy_check_mark:|
  |Where|:heavy_check_mark:|
  |Xor|:heavy_check_mark:|

  </div></details>

## Demo
Video speed is adjusted approximately 50 times slower than actual speed.
![render1665941718294](https://user-images.githubusercontent.com/33194443/196049928-57520fc2-842d-459c-9f28-7ee5f040c226.gif)

## Environment
- Linux / Windows
- onnx==1.13.1
- onnxruntime==1.15.0
- onnx-simplifier==0.4.33
- onnx_graphsurgeon
- simple_onnx_processing_tools
- tensorflow==2.13.0
- psutil==5.9.5
- flatbuffers-compiler (Optional, Only when using the `-coion` option. Executable file named `flatc`.)
  ```bash
  # Custom flatc binary for Ubuntu 20.04+
  # https://github.com/PINTO0309/onnx2tf/issues/196
  wget https://github.com/PINTO0309/onnx2tf/releases/download/1.7.3/flatc.tar.gz \
    && tar -zxvf flatc.tar.gz \
    && sudo chmod +x flatc \
    && sudo mv flatc /usr/bin/

  # Custom flatc binary for Windows
  # Set the environment variable paths appropriately on your own.
  # https://github.com/PINTO0309/onnx2tf/issues/196
  https://github.com/PINTO0309/onnx2tf/releases/download/1.7.3/flatc.exe
  ```

## Sample Usage
### 1. Install
- HostPC
  - When using GHCR, see `Authenticating to the Container registry`

    https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry
  ```bash
  # PAT authentication is required to pull from GHCR.
  $ docker login ghcr.io
  Username (xxxx): {Enter}
  Password: {Personal Access Token}
  Login Succeeded

  $ docker run --rm -it \
  -v `pwd`:/workdir \
  -w /workdir \
  ghcr.io/pinto0309/onnx2tf:1.15.3

  or

  # Authentication is not required for pulls from Docker Hub.
  $ docker run --rm -it \
  -v `pwd`:/workdir \
  -w /workdir \
  docker.io/pinto0309/onnx2tf:1.15.3

  or

  $ pip install -U onnx==1.13.1 \
  && pip install -U nvidia-pyindex \
  && pip install -U onnx-graphsurgeon \
  && pip install -U onnxruntime==1.15.0 \
  && pip install -U onnxsim==0.4.33 \
  && pip install -U simple_onnx_processing_tools \
  && pip install -U onnx2tf \
  && pip install -U h5py==3.7.0 \
  && pip install -U psutil==5.9.5

  or

  $ pip install -e .
  ```

or

- Google Colaboratory Python3.10
  ```
  !sudo apt-get -y update
  !sudo apt-get -y install python3-pip
  !sudo apt-get -y install python-is-python3
  !wget https://github.com/PINTO0309/onnx2tf/releases/download/1.7.3/flatc.tar.gz \
    && tar -zxvf flatc.tar.gz \
    && sudo chmod +x flatc \
    && sudo mv flatc /usr/bin/
  !pip install -U pip \
    && pip install tensorflow==2.13.0 \
    && pip install -U onnx==1.13.1 \
    && python -m pip install onnx_graphsurgeon \
          --index-url https://pypi.ngc.nvidia.com \
    && pip install -U onnxruntime==1.15.0 \
    && pip install -U onnxsim==0.4.33 \
    && pip install -U simple_onnx_processing_tools \
    && pip install -U onnx2tf \
    && pip install -U protobuf==3.20.3 \
    && pip install -U h5py==3.7.0 \
    && pip install -U psutil==5.9.5
  ```

### 2. Run test
Only patterns that are considered to be used particularly frequently are described. In addition, there are several other options, such as disabling Flex OP and additional options to improve inference performance. See: [CLI Parameter](#cli-parameter)
```bash
# Float32, Float16
# This is the fastest way to generate tflite,
# but the accompanying saved_model will not have a signature.
# "ValueError: Only support at least one signature key."
# If you are having trouble with this error, please use the `-osd` option.
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx

# saved_model with signaturedefs added.
# Output in the form of saved_model that can be used for serving
# or conversion to other frameworks. e.g. TensorFlow.js, CoreML, etc
# https://github.com/PINTO0309/onnx2tf#12-conversion-to-tensorflowjs
# https://github.com/PINTO0309/onnx2tf#13-conversion-to-coreml
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx -osd

# Override undefined batch size or other dimensions with static values.
# If the model has undefined dimensions, rewriting them to a static size will significantly
# improve the success rate of the conversion.
# The `-b` option overwrites the zero-dimensional batch size with the number specified
# without input OP name.
# Note that if there are multiple input OPs, the zero dimension of all input OPs is
# forced to be rewritten.
# The `-ois` option allows undefined dimensions in all dimensions, including
# the zero dimensionality, to be overwritten to a static shape, but requires
# the input OP name to be specified.
# e.g. -ois data1:1,3,224,224 data2:1,255 data3:1,224,6
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx -b 1
or
$ onnx2tf -i resnet18-v1-7.onnx -ois data:1,3,224,224

# Suppress automatic transposition of input OPs from NCW, NCHW, NCDHW to NWC, NHWC, NDHWC.
# onnx2tf is a specification that automatically transposes the input OP to [N,H,W,C] format
# before converting the model. However, since onnx2tf cannot determine from the structure of
# the model whether the input data is image, audio data, or something else, it unconditionally
# transposes the channels. Therefore, it is the models of STT/TTS models where the input is
# not NHWC that tend to have particular problems with the automatic transposition of the
# input OP.
# If you do not want input OPs to be automatically transposed, you can disable automatic
# transposition of input OPs by specifying the `-kat` option.
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/1.1.28/double_gru.onnx
# INPUT OPs: "spec": float32[1,3,257,1], "states_in": float32[2,1,32]
# The following command suppresses the automatic transposition of "states_in" and converts it.
$ onnx2tf -i double_gru.onnx -kat states_in

# Keras h5 format
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx -oh5

# Keras keras_v3 format (TensorFlow v2.12.0 or later only)
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx -okv3

# TensorFlow v1 (.pb) format
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/0.0.2/resnet18-v1-7.onnx
$ onnx2tf -i resnet18-v1-7.onnx -otfv1pb

# INT8 Quantization, Full INT8 Quantization
# INT8 Quantization with INT16 activation, Full INT8 Quantization with INT16 activation
# Dynamic Range Quantization
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/1.1.1/emotion-ferplus-8.onnx
# INT8 Quantization (per-channel)
$ onnx2tf -i emotion-ferplus-8.onnx -oiqt
# INT8 Quantization (per-tensor)
$ onnx2tf -i emotion-ferplus-8.onnx -oiqt -qt per-tensor

# Split the model at the middle position for debugging
# Specify the output name of the OP
$ onnx2tf -i resnet18-v1-7.onnx -onimc resnetv15_stage2_conv1_fwd resnetv15_stage2_conv2_fwd

# Suppress generation of Flex OP and replace with Pseudo-Function
# [Asin, Acos, Atan, Abs, PReLU, LeakyReLU, Power, GatherND, Neg, HardSwish, Erf]
# Below is a sample of replacing GELU / Erf with another set of operations.
$ wget https://s3.ap-northeast-2.wasabisys.com/temp-models/onnx2tf_readme/gelu_11.onnx
$ onnx2tf -i gelu_11.onnx -rtpo Erf

# High-dimensional Transpose decomposition
# If you do not like FlexTranspose being generated, try `-nodafc`.
# Suppresses the generation of FlexTranspose by decomposing Transpose
# to the specified number of dimensions.
# In TensorFlow v2.12.0 and later, up to 6 dimensions are converted to normal Transpose;
# in v2.11.0 and earlier, up to 5 dimensions are converted to normal Transpose.
# Note that specifying `2` for the `-nodafc` option causes all Transpose OPs to disappear
# from the model structure.
# Below is an example of decomposing a Transpose of 5 or more dimensions into a Transpose
# of 4 dimensions.
$ onnx2tf -i xxxx.onnx -nodafc 4

# Parameter replacement (Resize,Transpose,Softmax)
$ rm replace.json
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/1.1.27/human_segmentation_pphumanseg_2021oct.onnx
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/1.1.27/replace.json
$ onnx2tf -i human_segmentation_pphumanseg_2021oct.onnx -prf replace.json
```

### 3. Accuracy check
Perform error checking of ONNX output and TensorFlow output. Verify that the error of all outputs, one operation at a time, is below a certain threshold. Automatically determines before and after which OPs the tool's automatic conversion of the model failed. Know where dimensional compression, dimensional expansion, and dimensional transposition by `Reshape` and `Traspose` are failing. Once you have identified the problem area, you can refer to the tutorial on [Parameter replacement](#parameter-replacement) to modify the tool's behavior.

`-ois` an option to overwrite the input OP to a static size if it has undefined dimensions. `-cotof` option checks the accuracy of all OPs one by one. `-cotoa` is the error value of the threshold for determining an accuracy error. If there are undefined dimensions in the input OP, it is better to fix them to the static geometry to improve the accuracy of the accuracy measurement.

Also, you can use the `-cind` option to specify custom input for `-cotof`, instead of using the default dummy input. Otherwise, all input values will be set to 1. For more information about the `-cind` option, please refer to [here](#cli-parameter).

The `-cotof` option only compares the original ONNX and converted TensorFlow (Keras) models at Float32 precision, not at Float16 or INT8 precision.

```
$ onnx2tf -i mobilenetv2-12.onnx -ois input:1,3,224,224 -cotof -cotoa 1e-1

or

$ onnx2tf -i mobilenetv2-12.onnx -b 1 -cotof -cotoa 1e-1

or

$ onnx2tf -i mobilenetv2-12.onnx -cotof -cotoa 1e-1 -cind "input" "/your/path/x.npy"
```
![image](https://user-images.githubusercontent.com/33194443/216901668-5fdb1e38-8670-46a4-b4b9-8a774fa7545e.png)

![Kazam_screencast_00108_](https://user-images.githubusercontent.com/33194443/212460284-f3480105-4d94-4519-94dc-320d641f5647.gif)

### 4. Match tflite input/output names and input/output order to ONNX
If you want to match tflite's input/output OP names and the order of input/output OPs with ONNX, you can use the `interpreter.get_signature_runner()` to infer this after using the `-coion` / `--copy_onnx_input_output_names_to_tflite` option to output tflite file. See: https://github.com/PINTO0309/onnx2tf/issues/228
```python
import torch
import onnxruntime
import numpy as np
import onnx2tf
import tensorflow as tf
from tensorflow.lite.python import interpreter as tflite_interpreter

class Model(torch.nn.Module):
    def forward(self, x, y):
        return {
            "add": x + y,
            "sub": x - y,
        }

# Let's double check what PyTorch gives us
model = Model()
pytorch_output = model.forward(10, 2)
print("[PyTorch] Model Predictions:", pytorch_output)

# First, export the above model to ONNX
torch.onnx.export(
    Model(),
    {"x": 10, "y": 2},
    "model.onnx",
    opset_version=16,
    input_names=["x", "y"],
    output_names=["add", "sub"],
)

# And check its output
session = onnxruntime.InferenceSession("model.onnx")
onnx_output = session.run(["add", "sub"], {"x": np.array(10), "y": np.array(2)})
print("[ONNX] Model Outputs:", [o.name for o in session.get_outputs()])
print("[ONNX] Model Predictions:", onnx_output)

# Now, let's convert the ONNX model to TF
onnx2tf.convert(
    input_onnx_file_path="model.onnx",
    output_folder_path="model.tf",
    copy_onnx_input_output_names_to_tflite=True,
    non_verbose=True,
)

# Now, test the newer TFLite model
interpreter = tf.lite.Interpreter(model_path="model.tf/model_float32.tflite")
tf_lite_model = interpreter.get_signature_runner()
inputs = {
  'x': np.asarray([10], dtype=np.int64),
  'y': np.asarray([2], dtype=np.int64),
}
tf_lite_output = tf_lite_model(**inputs)
print("[TFLite] Model Predictions:", tf_lite_output)
```
```
[PyTorch] Model Predictions:
  {
    'add': 12,
    'sub': 8
  }
[ONNX] Model Outputs:
  [
    'add',
    'sub'
  ]
[ONNX] Model Predictions:
  [
    array(12, dtype=int64),
    array(8, dtype=int64)
  ]
[TFLite] Model Predictions:
  {
    'add': array([12]),
    'sub': array([8])
  }
```
![image](https://user-images.githubusercontent.com/33194443/223318437-b89e56c1-4376-4e91-8c0c-08d29a604637.png)

### 5. Rewriting of tflite input/output OP names and `signature_defs`
If you do not like tflite input/output names such as `serving_default_*:0` or `StatefulPartitionedCall:0`, you can rewrite them using the following tools and procedures. It can be rewritten from any name to any name, so it does not have to be `serving_default_*:0` or `StatefulPartitionedCall:0`.

https://github.com/PINTO0309/tflite-input-output-rewriter

```bash
# Install custom flatc
$ wget https://github.com/PINTO0309/onnx2tf/releases/download/1.7.3/flatc.tar.gz \
    && tar -zxvf flatc.tar.gz \
    && sudo chmod +x flatc \
    && sudo mv flatc /usr/bin/ \
    && rm flatc.tar.gz

# Path check
$ which flatc
/usr/bin/flatc

# Install tfliteiorewriter
$ pip install -U tfliteiorewriter
```
- Before

  ![01](https://github.com/PINTO0309/onnx2tf/assets/33194443/967ea56f-f771-4ccd-bdad-e4db41710396)

  ```bash
  $ tfliteiorewriter \
  -i xxxx.tflite \
  -r serving_default_input_1:0 aaa \
  -r StatefulPartitionedCall:0 bbb
  ```
  ![02](https://github.com/PINTO0309/onnx2tf/assets/33194443/841ce41e-dd3e-4156-883d-888d89e507c3)

- After

  ![03](https://github.com/PINTO0309/onnx2tf/assets/33194443/f7b7be16-c69c-4593-b8b5-e1cc23e61be9)


### 6. Embed metadata in tflite
If you want to embed label maps, quantization parameters, descriptions, etc. into your tflite file, you can refer to the official tutorial and try it yourself. For now, this tool does not plan to implement the ability to append metadata, as I do not want to write byte arrays to the tflite file that are not essential to its operation.

- Adding metadata to TensorFlow Lite models

  https://www.tensorflow.org/lite/models/convert/metadata
  ![image](https://user-images.githubusercontent.com/33194443/221345428-639ffa41-a03c-4d0b-bd72-9c23fb3847f3.png)

### 7. If the accuracy of the INT8 quantized model degrades significantly
It is a matter of model structure. The activation function (`SiLU`/`Swish`), kernel size and stride for `Pooling`, and kernel size and stride for `Conv` should be completely revised. See: https://github.com/PINTO0309/onnx2tf/issues/244#issuecomment-1475128445, and  https://github.com/PINTO0309/onnx2tf/issues/269

If you want to see the difference in quantization error between `SiLU` and `ReLU`, please check this Gist by [@motokimura](https://gist.github.com/motokimura) who helped us in our research. Thanks Motoki!

Gist: [Quantization error simulation of SiLU (Swish) activation](https://gist.github.com/motokimura/1a90c0b8c5628914b99a81cd91369636)

The accuracy error rates after quantization for different activation functions are shown in the figure below. The graph plots the distribution of absolute error, so a position with a higher value on the horizontal axis indicates a larger error. The vertical axis is the number of samples. `SiLU (Swish)` produces catastrophic errors after INT8 quantization.

![image](https://user-images.githubusercontent.com/33194443/226542318-aa7fc743-ffde-4245-b15f-b38b433ce28a.png)

- e.g. YOLOv8
  - https://docs.openvino.ai/latest/notebooks/230-yolov8-optimization-with-output.html
- e.g. YOLOX-Nano
  - https://github.com/motokimura/yolox-ti-lite_tflite
  - https://github.com/TexasInstruments/edgeai-yolox
    |Before|After|
    |:-:|:-:|
    |`Swish`/`SiLU`<br>![image](https://user-images.githubusercontent.com/33194443/226184543-408e0814-3c75-42f6-a640-377004982ba3.png)|`ReLU`<br>![image](https://user-images.githubusercontent.com/33194443/226184570-af4df0aa-e0d2-4fd7-afca-50dc6622977d.png)|
    |`DepthwiseConv2D`<br>![image](https://user-images.githubusercontent.com/33194443/226185407-ebf3f26d-a483-4fdd-8b27-266e4ba149ab.png)|`Conv2D`<br>![image](https://user-images.githubusercontent.com/33194443/226185388-2d2afa7e-6fd6-44a7-b0bc-705a5b22f036.png)|
    |`MaxPool`, kernel_size=5x5,9x9,13x13<br>![image](https://user-images.githubusercontent.com/33194443/226184640-8f942741-1109-4a95-b8da-ca49885879cd.png)|`MaxPool`, kernel_size=3x3<br>![image](https://user-images.githubusercontent.com/33194443/226184604-2c289b9d-7c15-4f84-b4ce-2838ecf4e6d0.png)|

    ```
    ### Float32 - YOLOX-Nano
    (1, 52, 52, 85)
    array([[[
        [ 0.971787,  0.811184,  0.550566, ..., -5.962632, -7.403673, -6.735206],
        [ 0.858804,  1.351296,  1.231673, ..., -6.479690, -8.277064, -7.664936],
        [ 0.214827,  1.035119,  1.458006, ..., -6.291425, -8.229385, -7.761562],
            ...,
        [ 0.450116,  1.391900,  1.533354, ..., -5.672194, -7.121591, -6.880231],
        [ 0.593133,  2.112723,  0.968755, ..., -6.150078, -7.370633, -6.874294],
        [ 0.088263,  1.985220,  0.619998, ..., -5.507928, -6.914980, -6.234259]]]]),

    ### INT8 - YOLOX-Nano
    (1, 52, 52, 85)
    array([[[
        [ 0.941908,  0.770652,  0.513768, ..., -5.993958, -7.449634, -6.850238],
        [ 0.856280,  1.284420,  1.198792, ..., -6.507727, -8.391542, -7.792146],
        [ 0.256884,  0.941908,  1.455676, ..., -6.336471, -8.305914, -7.877774],
            ...,
        [ 0.342512,  1.370048,  1.541304, ..., -5.737075, -7.192750, -7.107122],
        [ 0.513768,  2.226327,  1.027536, ..., -6.165215, -7.449634, -7.021494],
        [ 0.085628,  2.055072,  0.685024, ..., -5.480191, -7.021494, -6.422099]]]]),
    ```

- Other recommended replacement OP

    |Before|After|
    |:-:|:-:|
    |`HardSwish`<br>![image](https://user-images.githubusercontent.com/33194443/226223099-c7344bcf-d24d-4b35-a1d6-2a03dbfce8c7.png)|`ReLU`<br>![image](https://user-images.githubusercontent.com/33194443/226223213-bd714994-f353-416e-9f54-6d0954a70bb8.png)|
    |`ReLU6`<br>![image](https://user-images.githubusercontent.com/33194443/233639086-721e5e80-08c3-4785-9c1a-002bbfc0fa3d.png)<br>Paper: [A Quantization-Friendly Separable Convolution for MobileNets](https://arxiv.org/pdf/1803.08607.pdf) https://arxiv.org/pdf/1803.08607.pdf|`ReLU`<br>![image](https://user-images.githubusercontent.com/33194443/226223213-bd714994-f353-416e-9f54-6d0954a70bb8.png)|


### 8. Calibration data creation for INT8 quantization
Calibration data (.npy) for INT8 quantization (`-cind`) is generated as follows. This is a sample when the data used for training is image data. See: https://github.com/PINTO0309/onnx2tf/issues/222

https://www.tensorflow.org/lite/performance/post_training_quantization

```python
import cv2
import glob
import numpy as np

# Not used during data generation ################################
# You will need to do the calculations yourself using the test data
MEAN = np.asarray([[[[0.485, 0.456, 0.406]]]], dtype=np.float32) # [1,1,1,3]
STD = np.asarray([[[[0.229, 0.224, 0.225]]]], dtype=np.float32) # [1,1,1,3]
# Not used during data generation ################################

files = glob.glob("data/*.png")
img_datas = []
for idx, file in enumerate(files):
    bgr_img = cv2.imread(file)
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    resized_img = cv2.resize(rgb_img, dsize=(200,112))
    extend_batch_size_img = resized_img[np.newaxis, :]
    normalized_img = extend_batch_size_img / 255.0 # 0.0 - 1.0
    print(
        f'{str(idx+1).zfill(2)}. extend_batch_size_img.shape: {extend_batch_size_img.shape}'
    ) # [1,112,200,3]
    img_datas.append(extend_batch_size_img)
calib_datas = np.vstack(img_datas)
print(f'calib_datas.shape: {calib_datas.shape}') # [10,112,200,3]
np.save(file='data/calibdata.npy', arr=calib_datas)

loaded_data = np.load('data/calibdata.npy')
print(f'loaded_data.shape: {loaded_data.shape}') # [10,112,200,3]

"""
-cind INPUT_NAME NUMPY_FILE_PATH MEAN STD
int8_calib_datas = (loaded_data - MEAN) / STD # -1.0 - 1.0

e.g. How to specify calibration data in CLI or Script respectively.
1. CLI
  -cind "pc_dep" "data/calibdata.npy" "[[[[0.485,0.456,0.406]]]]" "[[[[0.229,0.224,0.225]]]]"
  -cind "feat" "data/calibdata2.npy" "[[[[0.123,...,0.321]]]]" "[[[[0.112,...,0.451]]]]"

2. Script
  custom_input_op_name_np_data_path=[
      ["pc_dep", "data/calibdata.npy", [[[[0.485,0.456,0.406]]]], [[[[0.229,0.224,0.225]]]]],
      ["feat", "data/calibdata2.npy", [[[[0.123,...,0.321]]]], [[[[0.112,...,0.451]]]],
  ]
"""
```

### 9. INT8 quantization of models with multiple inputs requiring non-image data
If you do not need to perform INT8 quantization with this tool alone, the following method is the easiest.

The `-osd` option will output a `saved_model.pb` in the `saved_model` folder with the full size required for quantization. That is, a default signature named `serving_default` is embedded in `.pb`. The `-b` option is used to convert the batch size by rewriting it as a static integer.

**Note: INT8 TFLite generated by following this procedure as is will result in a model with significantly degraded accuracy. This tutorial only demonstrates the INT8 quantization procedure; if you wish to correct for accuracy, please refer to [Parameter replacement](#parameter-replacement) to correct for transposition errors in the operation.**

```bash
# Ref: https://github.com/onnx/models/tree/main/text/machine_comprehension/bert-squad
wget https://s3.ap-northeast-2.wasabisys.com/temp-models/onnx2tf_248/bertsquad-12.onnx

onnx2tf -i bertsquad-12.onnx -b 1 -osd -cotof
```

![image](https://user-images.githubusercontent.com/33194443/225175510-95200964-06ff-474a-8cd4-f640bec6c397.png)

Use the `saved_model_cli` command to check the `saved_model` signature. INT8 quantization calibration using signatures allows correct control of the input order of data for calibration. Therefore, calibration with signatures is recommended for INT8 quantization of models with multiple inputs.

```bash
saved_model_cli show --dir saved_model/ --tag_set serve --signature_def serving_default

The given SavedModel SignatureDef contains the following input(s):
  inputs['input_ids_0'] tensor_info:
      dtype: DT_INT64
      shape: (1, 256)
      name: serving_default_input_ids_0:0
  inputs['input_mask_0'] tensor_info:
      dtype: DT_INT64
      shape: (1, 256)
      name: serving_default_input_mask_0:0
  inputs['segment_ids_0'] tensor_info:
      dtype: DT_INT64
      shape: (1, 256)
      name: serving_default_segment_ids_0:0
  inputs['unique_ids_raw_output___9_0'] tensor_info:
      dtype: DT_INT64
      shape: (1)
      name: serving_default_unique_ids_raw_output___9_0:0
```

Calibrate by specifying the input OP name displayed in `inputs`. The `np.ones([xxx], dtype=np.int64)` part must be replaced with the correct calibration test data. In practice, several pieces of data used for training are extracted and used.

```python
import tensorflow as tf
import numpy as np

def representative_dataset():
    unique_ids = np.ones([10, 256], dtype=np.int64)
    segment_ids = np.ones([10, 256], dtype=np.int64)
    input_masks = np.ones([10, 256], dtype=np.int64)
    input_ids = np.ones([10], dtype=np.int64)

    for unique_id, segment_id, input_mask, input_id \
        in zip(unique_ids, segment_ids, input_masks, input_ids):

        yield {
            "unique_ids_raw_output___9_0": unique_id,
            "segment_ids_0": segment_id,
            "input_mask_0": input_mask,
            "input_ids_0": input_id,
        }

converter = tf.lite.TFLiteConverter.from_saved_model('saved_model')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8  # or tf.uint8
converter.inference_output_type = tf.int8  # or tf.uint8
tflite_quant_model = converter.convert()

with open('saved_model/int8_model.tflite', 'wb') as w:
    w.write(tflite_quant_model)
```

![image](https://user-images.githubusercontent.com/33194443/225174599-e62173f3-1dd2-48f4-a762-f15ef78cd01e.png)

https://www.tensorflow.org/lite/performance/post_training_quantization

See: https://github.com/PINTO0309/onnx2tf/issues/248

### 10. Fixing the output of NonMaxSuppression (NMS)
PyTorch's `NonMaxSuppression (torchvision.ops.nms)` and ONNX's `NonMaxSuppression` are not fully compatible. TorchVision's NMS is very inefficient. Therefore, it is inevitable that converting ONNX using NMS in object detection models and other models will be very redundant and will be converted with a structure that is difficult for TensorFlow.js and TFLite models to take advantage of in devices. This is due to the indefinite number of tensors output by the NMS. In this chapter, I share how to easily tune the ONNX generated using TorchVision's redundant NMS to generate an optimized NMS.

1. There are multiple issues with TorchVision's NMS. First, the batch size specification is not supported; second, the `max_output_boxes_per_class` parameter cannot be specified. Please see the NMS sample ONNX part I generated. The `max_output_boxes_per_class` has been changed to `896` instead of `-Infinity`. The biggest problem with TorchVision NMS is that it generates ONNX with `max_output_boxes_per_class` set to `-Infinity` or `9223372036854775807 (Maximum value of INT64)`, resulting in a variable number of NMS outputs from zero to infinite. Thus, by rewriting `-Infinity` or `9223372036854775807 (Maximum value of INT64)` to a constant value, it is possible to output an NMS that can be effortlessly inferred by TFJS or TFLite.
![image](https://user-images.githubusercontent.com/33194443/230778827-faab8ffe-d49f-498d-b414-a1a26848a380.png)

    Here you will find committed ONNX components optimized for various devices.
    https://github.com/PINTO0309/components_of_onnx/tree/main/components_of_onnx/ops

2. In the following example, the `max_output_boxes_per_class` of NMS in the post-processing generated by YOLOv7 is changed from `-Infinity` or `9223372036854775807 (Maximum value of INT64)` to `20`, as shown in the figure below. The name `main01_max_output_boxes_per_class` has been rewritten by me for clarity, but it originally appears as `max_output_boxes_per_class`.
![image](https://user-images.githubusercontent.com/33194443/230779419-23cc017f-fde9-4777-bb3d-766a35a09efd.png)

    Simply execute the following command. The command rewrites the specified attribute value of the OP specified by ONNX.
    ```bash
    pip install sam4onnx

    sam4onnx \
    --op_name main01_nonmaxsuppression11 \
    --input_onnx_file_path yolov7.onnx \
    --output_onnx_file_path nms_yolov7_update.onnx \
    --input_constants main01_max_output_boxes_per_class int64 [20]
    ```
    A tutorial on one of my ONNX modification tools, `sam4onnx`, can be found here.

    https://github.com/PINTO0309/sam4onnx

    Many detailed tutorials are provided below, so if you are interested, please play with them.

    https://github.com/PINTO0309/PINTO_model_zoo/tree/main/307_YOLOv7/post_process_gen_tools

3. Finally, simply convert ONNX to TFLite or saved_model or TFJS using onnx2tf. onnx2tf performs an internal operation to automatically optimize the NMS output to a fixed shape if `max_output_boxes_per_class` is set to a value other than `-Infinity` and `9223372036854775807 (Maximum value of INT64)`. Specify `--output_nms_with_dynamic_tensor` or `-onwdt` if you do not want to optimize for a fixed shape.
    ```
    onnx2tf -i nms_yolov7_update.onnx -osd -cotof
    ```
    I would be happy if this is a reference for Android + Java or TFJS implementations. There are tons more tricky model optimization techniques described in my blog posts, so you'll have to find them yourself. I don't dare to list the URL here because it is annoying to see so many `issues` being posted. And unfortunately, all articles are in Japanese.
    ![image](https://user-images.githubusercontent.com/33194443/230780749-9967a34b-abf6-47fe-827d-92e0f6bddf46.png)

### 11. RNN (RNN, GRU, LSTM) Inference Acceleration
TensorFlow's RNN has a speedup option called `unroll`. The network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. onnx2tf allows you to deploy RNNs into memory-intensive operations by specifying the `--enable_rnn_unroll` or `-eru` options. The `--enable_rnn_unroll` option is available for `RNN`, `GRU`, and `LSTM`.

- Keras https://keras.io/api/layers/recurrent_layers/lstm/
- TensorFlow https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM

An example of `BidirectionalLSTM` conversion with the `--enable_rnn_unroll` option is shown below. Please ignore that the shapes of the input and output tensors do not match, since the samples are shown by picking up separate models.

- ONNX `LSTM (Bidirectional)`

  ![image](https://user-images.githubusercontent.com/33194443/234157356-7a0790a5-d5e0-4d9b-9800-0750fc944ac6.png)

- `BidirectionalLSTM` with `--enable_rnn_unroll` option unspecified

  Recurrent layer is implemented from scratch.

  ![image](https://user-images.githubusercontent.com/33194443/234149979-4931a8cb-a2da-429a-a811-db46e1ca4c5e.png)

- `BidirectionalLSTM` with `--enable_rnn_unroll` option

  ![image](https://user-images.githubusercontent.com/33194443/234149995-7b68b550-90d9-4070-abd0-158d1e824315.png)

### 12. Conversion to TensorFlow.js
When converting to TensorFlow.js, process as follows.

```bash
pip install tensorflowjs

onnx2tf -i mobilenetv2-12.onnx -ois input:1,3,224,224 -osd

tensorflowjs_converter \
--input_format tf_saved_model \
--output_format tfjs_graph_model \
saved_model \
tfjs_model
```

See: https://github.com/tensorflow/tfjs/tree/master/tfjs-converter

![image](https://user-images.githubusercontent.com/33194443/224186149-0b9ce9dc-fe09-48d4-b430-6cc3d0687140.png)

### 13. Conversion to CoreML
When converting to CoreML, process as follows. The `-k` option is for conversion while maintaining the input channel order in ONNX's NCHW format.

```bash
pip install coremltools

onnx2tf -i mobilenetv2-12.onnx -k input -ois input:1,3,224,224 -osd
```
```python
import coremltools as ct

FOLDER_PATH = 'saved_model'

model = ct.convert(
    model=FOLDER_PATH,
    source='tensorflow',
)
model.save(f'{FOLDER_PATH}/model.mlmodel')
```

See: https://github.com/apple/coremltools

![image](https://user-images.githubusercontent.com/33194443/224185761-bd0c086c-65e8-4de7-a500-f49b666eea0a.png)

## CLI Parameter
```

$ onnx2tf -h

usage: onnx2tf
[-h]
(-i INPUT_ONNX_FILE_PATH | -V)
[-o OUTPUT_FOLDER_PATH]
[-osd]
[-oh5]
[-okv3]
[-otfv1pb]
[-ow]
[-coion]
[-oiqt]
[-qt {per-channel,per-tensor}]
[-cind INPUT_NAME NUMPY_FILE_PATH MEAN STD]
[-ioqd {int8,uint8}]
[-nuo]
[-nuonag]
[-b BATCH_SIZE]
[-ois OVERWRITE_INPUT_SHAPE [OVERWRITE_INPUT_SHAPE ...]]
[-nlt]
[-onwdt]
[-k KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES [KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES ...]]
[-kt KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES [KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES ...]]
[-kat KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES [KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES ...]]
[-onimc OUTPUT_NAMES [OUTPUT_NAMES ...]]
[-dgc]
[-ebu]
[-eru]
[-dsft]
[-nodaftc]
[-dsfs]
[-dsm]
[-nodafsc]
[-ofgd]
[-rari64 | -rarf32 | -rafi64 | -raff32]
[-fasr FUSED_ARGMAX_SCALE_RATIO]
[-rtpo REPLACE_TO_PSEUDO_OPERATORS [REPLACE_TO_PSEUDO_OPERATORS ...]]
[-me MVN_EPSILON]
[-prf PARAM_REPLACEMENT_FILE]
[-cgdc]
[-coto | -cotof]
[-coton]
[-cotor CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_RTOL]
[-cotoa CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_ATOL]
[-dms]
[-uc]
[-n]
[-v]

optional arguments:
  -h, --help
    show this help message and exit

  -i INPUT_ONNX_FILE_PATH, --input_onnx_file_path INPUT_ONNX_FILE_PATH
    Input onnx file path.

  -V, --version
    Show version and exit.

  -o OUTPUT_FOLDER_PATH, --output_folder_path OUTPUT_FOLDER_PATH
    Output folder path. Default: "saved_model"

  -osd, --output_signaturedefs
    Signature is added to the output for serving or for conversion
    to other model formats. However, this can significantly reduce the speed
    of model conversion and significant increase the size of the model.

  -oh5, --output_h5
    Output model in Keras (hdf5) format.

  -okv3, --output_keras_v3
    Output model in Keras (keras_v3) format.

  -otfv1pb, --output_tfv1_pb
    Output model in TF v1 (.pb) format.

  -ow, --output_weights
    Output weights in hdf5 format.

  -coion, --copy_onnx_input_output_names_to_tflite
    Copy the input/output OP name of ONNX to the input/output OP name of tflite.
    Due to Tensorflow internal operating specifications,
    the input/output order of ONNX does not necessarily match
    the input/output order of tflite.
    Be sure to check that the input/output OP names in the generated
    tflite file have been converted as expected.
    Also, this option generates a huge JSON file as a temporary file for processing.
    Therefore, it is strongly discouraged to use it on large models of hundreds
    of megabytes or more.

  -oiqt, --output_integer_quantized_tflite
    Output of integer quantized tflite.

  -qt {per-channel,per-tensor}, --quant_type {per-channel,per-tensor}
    Selects whether "per-channel" or "per-tensor" quantization is used.
    Default: "per-channel"

  -cind INPUT_NAME NUMPY_FILE_PATH MEAN STD, \
    --custom_input_op_name_np_data_path INPUT_NAME NUMPY_FILE_PATH MEAN STD
    Input name of OP and path of data file (Numpy) for custom input for -cotof or -oiqt,
    and mean (optional) and std (optional).

    <Usage in -cotof>
      When using -cotof, custom input defined by the user, instead of dummy data, is used.
      In this case, mean and std are omitted from the input.
      -cind {input_op_name} {numpy_file_path}
      e.g. -cind onnx::Equal_0 test_cind/x_1.npy -cind onnx::Add_1 test_cind/x_2.npy -cotof
      The input_op_name must be the same as in ONNX,
      and it may not work if the input format is different between ONNX and TF.

    <Usage in -oiqt>
      INPUT Name of OP and path of calibration data file (Numpy) for quantization
      and mean and std.
      The specification can be omitted only when the input OP is a single 4D tensor image data.
      If omitted, it is automatically calibrated using 20 normalized MS-COCO images.
      The type of the input OP must be Float32.
      Data for calibration must be pre-normalized to a range of 0 to 1.
      -cind {input_op_name} {numpy_file_path} {mean} {std}
      Numpy file paths must be specified the same number of times as the number of input OPs.
      Normalize the value of the input OP based on the tensor specified in mean and std.
      (input_value - mean) / std
      Tensors in Numpy file format must be in dimension order after conversion to TF.
      Note that this is intended for deployment on low-resource devices,
      so the batch size is limited to 1 only.

      e.g.
      The example below shows a case where there are three input OPs.
      Assume input0 is 128x128 RGB image data.
      In addition, input0 should be a value that has been divided by 255
      in the preprocessing and normalized to a range between 0 and 1.
      input1 and input2 assume the input of something that is not an image.
      Because input1 and input2 assume something that is not an image,
      the divisor is not 255 when normalizing from 0 to 1.
      "n" is the number of calibration data.

      ONNX INPUT shapes:
        input0: [n,3,128,128]
            mean: [1,3,1,1] -> [[[[0.485]],[[0.456]],[[0.406]]]]
            std:  [1,3,1,1] -> [[[[0.229]],[[0.224]],[[0.225]]]]
        input1: [n,64,64]
            mean: [1,64] -> [0.1, ..., 0.64]
            std:  [1,64] -> [0.05, ..., 0.08]
        input2: [n,5]
            mean: [1] -> [0.3]
            std:  [1] -> [0.07]
      TensorFlow INPUT shapes (Numpy file ndarray shapes):
        input0: [n,128,128,3]
            mean: [1,1,1,3] -> [[[[0.485, 0.456, 0.406]]]]
            std:  [1,1,1,3] -> [[[[0.229, 0.224, 0.225]]]]
        input1: [n,64,64]
            mean: [1,64] -> [0.1, ..., 0.64]
            std:  [1,64] -> [0.05, ..., 0.08]
        input2: [n,5]
            mean: [1] -> [0.3]
            std:  [1] -> [0.07]
      -cind "input0" "../input0.npy" "[[[[0.485,0.456,0.406]]]]" "[[[[0.229,0.224,0.225]]]]"
      -cind "input1" "./input1.npy" "[0.1,...,0.64]" "[0.05,...,0.08]"
      -cind "input2" "input2.npy" "[0.3]" "[0.07]"

    <Using -cotof and -oiqt at the same time>
      To use -cotof and -oiqt simultaneously,
      you need to enter the Input name of OP, path of data file, mean, and std all together.
      And the data file must be in Float32 format,
      and {input_op_name}, {numpy_file_path}, {mean}, and {std} must all be entered.
      Otherwise, an error will occur during the -oiqt stage.

  -ioqd {int8,uint8}, --input_output_quant_dtype {int8,uint8}
    Input and Output dtypes when doing Full INT8 Quantization.
    "int8"(default) or "uint8"

  -nuo, --not_use_onnxsim
    No optimization by onnx-simplifier is performed.
    If this option is used, the probability of a conversion error is very high.

  -nuonag, --not_use_opname_auto_generate
    Automatic generation of each OP name in the old format ONNX file
    and assignment of OP name are not performed.

  -b BATCH_SIZE, --batch_size BATCH_SIZE
    Fixes the dynamic batch size to the specified numeric batch size.
    A value of 1 or more must be specified.

  -ois OVERWRITE_INPUT_SHAPE [OVERWRITE_INPUT_SHAPE ...], \
      --overwrite_input_shape OVERWRITE_INPUT_SHAPE [OVERWRITE_INPUT_SHAPE ...]
    Overwrite the input shape.
    The format is
    "i1:dim0,...,dimN" "i2:dim0,...,dimN" "i3:dim0,...,dimN"
    When there is only one input, for example,
    "data:1,3,224,224"
    When there are multiple inputs, for example,
    "data1:1,3,224,224" "data2:1,3,112" "data3:5"
    A value of 1 or more must be specified.
    Numerical values other than dynamic dimensions are ignored.
    Ignores --batch_size if specified at the same time as --batch_size.

  -nlt, --no_large_tensor
    Suppresses constant bloat caused by Tile OP when optimizing models in onnxsim.
    See: https://github.com/daquexian/onnx-simplifier/issues/178

  -onwdt, --output_nms_with_dynamic_tensor
    The number of bounding boxes in the NMS output results is
    not fixed at the maximum number of max_output_boxes_per_class,
    but rather at the smallest possible number of dynamic tensors.
    If this option is disabled, NMS output is padded to the number
    set in the max_output_boxes_per_class attribute.
    e.g.
    disable --output_nms_with_dynamic_tensor:
        output_tensor_shape: [100, 7]
    enable --output_nms_with_dynamic_tensor:
        output_tensor_shape: [N, 7]

  -k KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES [KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES ...], \
      --keep_ncw_or_nchw_or_ncdhw_input_names KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES \
          [KEEP_NCW_OR_NCHW_OR_NCDHW_INPUT_NAMES ...]
    Holds the NCW or NCHW or NCDHW of the input shape for the specified INPUT OP names.
    If a nonexistent INPUT OP name is specified, it is ignored.
    Valid only for 3D, 4D and 5D input tensors.
    e.g. --keep_ncw_or_nchw_or_ncdhw_input_names "input0" "input1" "input2"

  -kt KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES [KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES ...], \
      --keep_nwc_or_nhwc_or_ndhwc_input_names KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES \
          [KEEP_NWC_OR_NHWC_OR_NDHWC_INPUT_NAMES ...]
    Holds the NWC or NHWC or NDHWC of the input shape for the specified INPUT OP names.
    If a nonexistent INPUT OP name is specified, it is ignored.
    If the input OP name is the same as the input OP name specified
    in the keep_ncw_or_nchw_or_ncdhw_input_names option, it is ignored.
    Valid only for 3D, 4D and 5D input tensors.
    e.g. --keep_nwc_or_nhwc_or_ndhwc_input_names "input0" "input1" "input2"

  -kat KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES [KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES ...], \
      --keep_shape_absolutely_input_names KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES \
        [KEEP_SHAPE_ABSOLUTELY_INPUT_NAMES ...]
    Name of the INPUT that unconditionally maintains its shape.
    If a nonexistent INPUT OP name is specified, it is ignored.
    e.g. --keep_shape_absolutely_input_names "input0" "input1" "input2"

  -onimc OUTPUT_NAMES [OUTPUT_NAMES ...], \
      --output_names_to_interrupt_model_conversion OUTPUT_NAMES [OUTPUT_NAMES ...]
    Output names of ONNX that interrupt model conversion.
    Interrupts model transformation at the specified output name and outputs the
    model partitioned into subgraphs.
    e.g. --output_names_to_interrupt_model_conversion "output0" "output1" "output2"

  -dgc, --disable_group_convolution
    Disable GroupConvolution and replace it with SeparableConvolution for
    output to saved_model format.

  -ebu, --enable_batchmatmul_unfold
    BatchMatMul is separated batch by batch to generate a primitive MatMul.

  -eru, --enable_rnn_unroll
    Instead of increasing inference speed by expanding all symbolic loops of
    the RNN (LSTM, GRU, RNN), RAM consumption will increase because all tensors
    are expanded and embedded in the model.
    https://keras.io/api/layers/recurrent_layers/

  -dsft, --disable_suppression_flextranspose
    Disables FlexTranspose generation suppression.

  -nodaftc, --number_of_dimensions_after_flextranspose_compression
    Number of Transpose OP dimensions generated after avoiding FlexTranspose generation.
    Also suppress the creation of the Transpose itself by specifying 2.
    Default: 6

  -dsfs, --disable_suppression_flexstridedslice
    Disables FlexStridedSlice generation suppression.

  -dsm, --disable_strict_mode
    If specified, the conversion speed is greatly accelerated because the strict accuracy
    correction process is skipped, but the frequency of transposition errors increases
    and accuracy errors are more likely to occur. Strict mode is enabled by default.
    As of 2023.05.07, this is a work in progress and is an experimental feature.
    Therefore, only some OPs are converted in strict mode for accuracy correction.

  -nodafsc, --number_of_dimensions_after_flexstridedslice_compression
    Number of StridedSlice OP dimensions generated after avoiding FlexStridedSlice generation.
    Default: 5

  -ofgd, --optimization_for_gpu_delegate
    Replace operations that do not support gpu delegate with those
    that do as much as possible.

  -rari64, --replace_argmax_to_reducemax_and_indicies_is_int64
    Replace ArgMax with a ReduceMax. The returned indicies are int64.
    Only one of replace_argmax_to_reducemax_and_indicies_is_int64
    and replace_argmax_to_reducemax_and_indicies_is_float32
    and replace_argmax_to_fused_argmax_and_indicies_is_int64
    and replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.

  -rarf32, --replace_argmax_to_reducemax_and_indicies_is_float32
    Replace ArgMax with a ReduceMax. The returned indicies are float32.
    Only one of replace_argmax_to_reducemax_and_indicies_is_int64
    and replace_argmax_to_reducemax_and_indicies_is_float32
    and replace_argmax_to_fused_argmax_and_indicies_is_int64
    and replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.

  -rafi64, --replace_argmax_to_fused_argmax_and_indicies_is_int64
    Replace ArgMax with a Fused_ArgMax. The returned indicies are int64.
    It improves inference speed at the cost of a small sacrifice in accuracy.
    See. https://github.com/tensorflow/models/tree/master/official/projects/edgetpu/vision#argmax-fusion-to-improve-segmentation-model-latency
    Currently, only 4D tensors are supported.
    Only one of replace_argmax_to_reducemax_and_indicies_is_int64
    and replace_argmax_to_reducemax_and_indicies_is_float32
    and replace_argmax_to_fused_argmax_and_indicies_is_int64
    and replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.

  -raff32, --replace_argmax_to_fused_argmax_and_indicies_is_float32
    Replace ArgMax with a Fused_ArgMax. The returned indicies are float32.
    It improves inference speed at the cost of a small sacrifice in accuracy.
    See. https://github.com/tensorflow/models/tree/master/official/projects/edgetpu/vision#argmax-fusion-to-improve-segmentation-model-latency
    Currently, only 4D tensors are supported.
    Only one of replace_argmax_to_reducemax_and_indicies_is_int64
    and replace_argmax_to_reducemax_and_indicies_is_float32
    and replace_argmax_to_fused_argmax_and_indicies_is_int64
    and replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.

  -fasr FUSED_ARGMAX_SCALE_RATIO, --fused_argmax_scale_ratio FUSED_ARGMAX_SCALE_RATIO
    For Fused ArgMax.
    Scale ratio when generating Fused ArgMax.
    0.0 < fused_argmax_scale_ratio <= 1.0
    Default: 0.5

  -rtpo, --replace_to_pseudo_operators
    Replace list of operators to pseudo operators.
    Full name of the target operators should be given.
    Currently supported operators :
    Asin, Acos, Atan, Abs, PReLU, LeakyReLU, Power, GatherND, Neg, HardSwish, Erf

  -me, --mvn_epsilon
    For MeanVarianceNormalization.
    The number to be added to the variance to avoid division by zero
    when normalizing the value.
    (input_tensor - mean) / tf.sqrt(variance + mvn_epsilon)
    Default: 0.0000000001

  -prf PARAM_REPLACEMENT_FILE, --param_replacement_file PARAM_REPLACEMENT_FILE
    Parameter replacement file path. (.json)

  -cgdc, --check_gpu_delegate_compatibility
    Run TFLite ModelAnalyzer on the generated Float16 tflite model
    to check if the model can be supported by GPU Delegate.
    e.g.
    """
    === TFLite ModelAnalyzer ===

    Your TFLite model has '1' subgraph(s). In the subgraph description below,
    T# represents the Tensor numbers. For example, in Subgraph#0, the RESHAPE op takes
    tensor #0 and tensor #6 as input and produces tensor #7 as output.

    Subgraph#0 main(T#0) -> [T#17]
      Op#0 RESHAPE(T#0, T#6[2, 8, 8, 3, 2, ...]) -> [T#7]
      Op#1 SPLIT(T#5[0], T#7) -> [T#8, T#9]
      Op#2 RESHAPE(T#8, T#1[8, 8, 3, 2, 2]) -> [T#10]
      Op#3 TRANSPOSE(T#10, T#4[0, 3, 1, 4, 2]) -> [T#11]
      Op#4 RESHAPE(T#11, T#2[1, 8, 2, 8, 2, ...]) -> [T#12]
      Op#5 RESHAPE(T#9, T#1[8, 8, 3, 2, 2]) -> [T#13]
      Op#6 TRANSPOSE(T#13, T#4[0, 3, 1, 4, 2]) -> [T#14]
      Op#7 RESHAPE(T#14, T#2[1, 8, 2, 8, 2, ...]) -> [T#15]
      Op#8 CONCATENATION(T#12, T#15) -> [T#16]
      Op#9 RESHAPE(T#16, T#3[2, 16, 16, 3]) -> [T#17]

    Tensors of Subgraph#0
      T#0(inputs_0) shape:[2, 8, 8, 12], type:FLOAT32
      T#1(model/tf.compat.v1.squeeze_2/Squeeze) shape:[5], type:INT32 RO 20 bytes, data:[8, 8, 3, 2, 2]
      T#2(model/tf.expand_dims_1/ExpandDims) shape:[6], type:INT32 RO 24 bytes, data:[1, 8, 2, 8, 2, ...]
      T#3(model/tf.reshape_1/Reshape/shape) shape:[4], type:INT32 RO 16 bytes, data:[2, 16, 16, 3]
      T#4(model/tf.compat.v1.transpose/transpose/perm) shape:[5], type:INT32 RO 20 bytes, data:[0, 3, 1, 4, 2]
      T#5(model/tf.concat/concat/axis) shape:[], type:INT32 RO 4 bytes, data:[0]
      T#6(model/tf.reshape/Reshape/shape) shape:[6], type:INT32 RO 24 bytes, data:[2, 8, 8, 3, 2, ...]
      T#7(model/tf.reshape/Reshape) shape:[2, 8, 8, 3, 2, 2], type:FLOAT32
      T#8(model/tf.split/split) shape:[1, 8, 8, 3, 2, 2], type:FLOAT32
      T#9(model/tf.split/split1) shape:[1, 8, 8, 3, 2, 2], type:FLOAT32
      T#10(model/tf.compat.v1.squeeze_1/Squeeze) shape:[8, 8, 3, 2, 2], type:FLOAT32
      T#11(model/tf.compat.v1.transpose/transpose) shape:[8, 2, 8, 2, 3], type:FLOAT32
      T#12(model/tf.expand_dims/ExpandDims) shape:[1, 8, 2, 8, 2, 3], type:FLOAT32
      T#13(model/tf.compat.v1.squeeze_2/Squeeze1) shape:[8, 8, 3, 2, 2], type:FLOAT32
      T#14(model/tf.compat.v1.transpose_1/transpose) shape:[8, 2, 8, 2, 3], type:FLOAT32
      T#15(model/tf.expand_dims_1/ExpandDims1) shape:[1, 8, 2, 8, 2, 3], type:FLOAT32
      T#16(model/tf.concat/concat) shape:[2, 8, 2, 8, 2, 3], type:FLOAT32
      T#17(Identity) shape:[2, 16, 16, 3], type:FLOAT32

    Your model looks compatibile with GPU delegate with TFLite runtime version 2.10.0.
    But it doesn't guarantee that your model works well with GPU delegate.
    There could be some runtime incompatibililty happen.
    ---------------------------------------------------------------
                  Model size:       2988 bytes
        Non-data buffer size:       2757 bytes (92.27 %)
      Total data buffer size:        231 bytes (07.73 %)
        (Zero value buffers):          4 bytes (00.13 %)

    * Buffers of TFLite model are mostly used for constant tensors.
      And zero value buffers are buffers filled with zeros.
      Non-data buffers area are used to store operators, subgraphs and etc.
      You can find more details from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema.fbs
    """

  -coto, --check_onnx_tf_outputs_elementwise_close
    Returns "Matches" if the output of onnx and the output of TF are
    within acceptable proximity element by element.
    Returns "Unmatched" if the output of onnx and the output of TF are
    not within acceptable proximity element by element.
    If the output of onnx is 1D, it returns "Skipped" and skips the comparison
    between the output of onnx and that of TF. This is because when undefined
    dimensions are present, a situation often arises where very large index
    values are compared, causing OutOfMemory.
    Only the output content of the models final output OP is checked.

  -cotof, --check_onnx_tf_outputs_elementwise_close_full
    Returns "Matches" if the output of onnx and the output of TF are
    within acceptable proximity element by element.
    Check the output of all OPs in sequence from the beginning,
    including all but the final output OP of the model.
    Returns "Unmatched" if the output of onnx and the output of TF are
    not within acceptable proximity element by element.
    If the output of onnx is 1D, it returns "Skipped" and skips the comparison
    between the output of onnx and that of TF. This is because when undefined
    dimensions are present, a situation often arises where very large index
    values are compared, causing OutOfMemory.
    It is very time consuming because it performs as many inferences as
    there are operations.

  -coton, --check_onnx_tf_outputs_sample_data_normalization
    norm: Validate using random data normalized to the range 0.0 to 1.0
    denorm: Validate using random data in the range 0.0 to 255.0
    If there is a normalization layer at the model's entry point, or
    if the model was trained on denormalized data, "denorm" must be specified.
    Default: "norm"

  -cotor CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_RTOL,\
    --check_onnx_tf_outputs_elementwise_close_rtol CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_RTOL
    The relative tolerance parameter.
    Default: 0.0

  -cotoa CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_ATOL,\
    --check_onnx_tf_outputs_elementwise_close_atol CHECK_ONNX_TF_OUTPUTS_ELEMENTWISE_CLOSE_ATOL
    The absolute tolerance parameter.
    Default: 1e-4

  -dms, --disable_model_save
    Does not save the converted model. For CIs RAM savings.

  -uc, --use_cuda
    CUDA is used for dummy inference during accuracy checks, but accuracy is degraded.
    Note that if you need to convert extended OPs such as com.microsoft.xxx,
    you must enable this flag.

  -n, --non_verbose
    Shorthand to specify a verbosity of "error".

  -v, --verbosity
    Change the level of information printed.
    Values are "debug", "info", "warn", and "error".
    Default: "debug" (for backwards compatability)
```

## In-script Usage
```python
>>> from onnx2tf import convert
>>> help(convert)

Help on function convert in module onnx2tf:

convert(
  input_onnx_file_path: Union[str, NoneType] = '',
  onnx_graph: Union[onnx.onnx_ml_pb2.ModelProto, NoneType] = None,
  output_folder_path: Union[str, NoneType] = 'saved_model',
  output_signaturedefs: Optional[bool] = False,
  output_h5: Optional[bool] = False,
  output_keras_v3: Optional[bool] = False,
  output_tfv1_pb: Optional[bool] = False,
  output_weights: Optional[bool] = False,
  copy_onnx_input_output_names_to_tflite: Optional[bool] = False,
  output_integer_quantized_tflite: Optional[bool] = False,
  quant_type: Optional[str] = 'per-channel',
  custom_input_op_name_np_data_path: Optional[List] = None,
  input_output_quant_dtype: Optional[str] = 'int8',
  not_use_onnxsim: Optional[bool] = False,
  not_use_opname_auto_generate: Optional[bool] = False,
  batch_size: Union[int, NoneType] = None,
  overwrite_input_shape: Union[List[str], NoneType] = None,
  no_large_tensor: Optional[bool] = False,
  output_nms_with_dynamic_tensor: Optional[bool] = False,
  keep_ncw_or_nchw_or_ncdhw_input_names: Union[List[str], NoneType] = None,
  keep_nwc_or_nhwc_or_ndhwc_input_names: Union[List[str], NoneType] = None,
  keep_shape_absolutely_input_names: Optional[List[str]] = None,
  output_names_to_interrupt_model_conversion: Union[List[str], NoneType] = None,
  disable_group_convolution: Union[bool, NoneType] = False,
  enable_batchmatmul_unfold: Optional[bool] = False,
  enable_rnn_unroll: Optional[bool] = False,
  disable_suppression_flextranspose: Optional[bool] = False,
  number_of_dimensions_after_flextranspose_compression: Optional[int] = 6,
  disable_suppression_flexstridedslice: Optional[bool] = False,
  disable_strict_mode: Optional[bool] = False,
  number_of_dimensions_after_flexstridedslice_compression: Optional[int] = 5,
  optimization_for_gpu_delegate: Optional[bool] = False,
  replace_argmax_to_reducemax_and_indicies_is_int64: Union[bool, NoneType] = False,
  replace_argmax_to_reducemax_and_indicies_is_float32: Union[bool, NoneType] = False,
  replace_argmax_to_fused_argmax_and_indicies_is_int64: Union[bool, NoneType] = False,
  replace_argmax_to_fused_argmax_and_indicies_is_float32: Union[bool, NoneType] = False,
  fused_argmax_scale_ratio: Union[float, NoneType] = 0.5,
  replace_to_pseudo_operators: List[str] = None,
  mvn_epsilon: Union[float, NoneType] = 0.0000000001,
  param_replacement_file: Optional[str] = '',
  check_gpu_delegate_compatibility: Optional[bool] = False,
  check_onnx_tf_outputs_elementwise_close: Optional[bool] = False,
  check_onnx_tf_outputs_elementwise_close_full: Optional[bool] = False,
  check_onnx_tf_outputs_sample_data_normalization: Optional[str] = 'norm',
  check_onnx_tf_outputs_elementwise_close_rtol: Optional[float] = 0.0,
  check_onnx_tf_outputs_elementwise_close_atol: Optional[float] = 1e-4,
  disable_model_save: Union[bool, NoneType] = False,
  use_cuda: Union[bool, NoneType] = False,
  non_verbose: Union[bool, NoneType] = False,
  verbosity: Optional[str] = 'debug'
) -> keras.engine.training.Model

    Convert ONNX to TensorFlow models.

    Parameters
    ----------
    input_onnx_file_path: Optional[str]
      Input onnx file path.
      Either input_onnx_file_path or onnx_graph must be specified.

    onnx_graph: Optional[onnx.ModelProto]
      onnx.ModelProto.
      Either input_onnx_file_path or onnx_graph must be specified.
      onnx_graph If specified, ignore input_onnx_file_path and process onnx_graph.

    output_folder_path: Optional[str]
      Output tensorflow model folder path.
      Default: "saved_model"

    output_signaturedefs: Optional[bool]
      Signature is added to the output for serving or for conversion
      to other model formats. However, this can significantly reduce the speed
      of model conversion and significant increase the size of the model.

    output_h5: Optional[bool]
      Output model in Keras H5 format.

    output_keras_v3: Optional[bool]
      Output model in Keras (keras_v3) format.

    output_tfv1_pb: Optional[bool]
      Output model in TF v1 (.pb) format.

    output_weights: Optional[bool]
      Output weights in hdf5 format.

    copy_onnx_input_output_names_to_tflite: Optional[bool]
      Copy the input/output OP name of ONNX to the input/output OP name of tflite.
      Due to Tensorflow internal operating specifications,
      the input/output order of ONNX does not necessarily match
      the input/output order of tflite.
      Be sure to check that the input/output OP names in the generated
      tflite file have been converted as expected.
      Also, this option generates a huge JSON file as a temporary file for processing.
      Therefore, it is strongly discouraged to use it on large models of hundreds
      of megabytes or more.

    output_integer_quantized_tflite: Optional[bool]
      Output of integer quantized tflite.

    quant_type: Optional[str]
      Selects whether "per-channel" or "per-tensor" quantization is used.
      Default: "per-channel"

    custom_input_op_name_np_data_path: Optional[List]
      --custom_input_op_name_np_data_path INPUT_NAME NUMPY_FILE_PATH MEAN STD
      Input name of OP and path of data file (Numpy) for custom input for -cotof or -oiqt,
      and mean (optional) and std (optional).

      <Usage in -cotof>
        When using -cotof, custom input defined by the user, instead of dummy data, is used.
        In this case, mean and std are omitted from the input.
        -cind {input_op_name} {numpy_file_path}
        e.g. -cind onnx::Equal_0 test_cind/x_1.npy -cind onnx::Add_1 test_cind/x_2.npy -cotof
        The input_op_name must be the same as in ONNX,
        and it may not work if the input format is different between ONNX and TF.

      <Usage in -oiqt>
        INPUT Name of OP and path of calibration data file (Numpy) for quantization
        and mean and std.
        The specification can be omitted only when the input OP is a single 4D tensor image data.
        If omitted, it is automatically calibrated using 20 normalized MS-COCO images.
        The type of the input OP must be Float32.
        Data for calibration must be pre-normalized to a range of 0 to 1.
        -cind {input_op_name} {numpy_file_path} {mean} {std}
        Numpy file paths must be specified the same number of times as the number of input OPs.
        Normalize the value of the input OP based on the tensor specified in mean and std.
        (input_value - mean) / std
        Tensors in Numpy file format must be in dimension order after conversion to TF.
        Note that this is intended for deployment on low-resource devices,
        so the batch size is limited to 1 only.
        e.g.
        The example below shows a case where there are three input OPs.
        Assume input0 is 128x128 RGB image data.
        In addition, input0 should be a value that has been divided by 255
        in the preprocessing and normalized to a range between 0 and 1.
        input1 and input2 assume the input of something that is not an image.
        Because input1 and input2 assume something that is not an image,
        the divisor is not 255 when normalizing from 0 to 1.
        "n" is the number of calibration data.

        ONNX INPUT shapes:
          input0: [n,3,128,128]
            mean: [1,3,1,1] -> [[[[0.485]],[[0.456]],[[0.406]]]]
            std : [1,3,1,1] -> [[[[0.229]],[[0.224]],[[0.225]]]]
          input1: [n,64,64]
            mean: [1,64] -> [[0.1, ..., 0.64]]
            std : [1,64] -> [[0.05, ..., 0.08]]
          input2: [n,5]
            mean: [1] -> [0.3]
            std : [1] -> [0.07]

        TensorFlow INPUT shapes (Numpy file ndarray shapes):
          input0: [n,128,128,3]
            mean: [1,1,1,3] -> [[[[0.485, 0.456, 0.406]]]]
            std : [1,1,1,3] -> [[[[0.229, 0.224, 0.225]]]]
          input1: [n,64,64]
            mean: [1,64] -> [[0.1, ..., 0.64]]
            std : [1,64] -> [[0.05, ..., 0.08]]
          input2: [n,5]
            mean: [1] -> [0.3]
            std : [1] -> [0.07]

          cind=[
              ["input0","../input0.npy",[[[[0.485, 0.456, 0.406]]]],[[[[0.229, 0.224, 0.225]]]]],
              ["input1","./input1.npy",[0.1, ..., 0.64],[0.05, ..., 0.08]],
              ["input2","input2.npy",[0.3],[0.07]],
          ]

      <Using -cotof and -oiqt at the same time>
        To use -cotof and -oiqt simultaneously,
        you need to enter the Input name of OP, path of data file, mean, and std all together.
        And the data file must be in Float32 format,
        and {input_op_name}, {numpy_file_path}, {mean}, and {std} must all be entered.
        Otherwise, an error will occur during the -oiqt stage.

    input_output_quant_dtype: Optional[str]
      Input and Output dtypes when doing Full INT8 Quantization.
      "int8"(default) or "uint8"

    not_use_onnxsim: Optional[bool]
      No optimization by onnx-simplifier is performed.
      If this option is used, the probability of a conversion error is very high.

    not_use_opname_auto_generate: Optional[bool]
      Automatic generation of each OP name in the old format ONNX file
      and assignment of OP name are not performed.

    batch_size: Optional[int]
      Fixes the dynamic batch size to the specified numeric batch size.
      A value of 1 or more must be specified.

    overwrite_input_shape: Optional[List[str]]
      Overwrite the input shape.
      The format is
      ['i1:dim0,dim1,...,dimN', 'i2:dim0,dim1,...,dimN', 'i3:dim0,dim1,...,dimN']
      When there is only one input, for example,
      ['data:1,3,224,224']
      When there are multiple inputs, for example,
      ['data1:1,3,224,224','data2:1,3,112','data3:5']
      A value of 1 or more must be specified.
      Numerical values other than dynamic dimensions are ignored.
      Ignores batch_size if specified at the same time as batch_size.

    no_large_tensor: Optional[bool]
      Suppresses constant bloat caused by Tile OP when optimizing models in onnxsim.
      See: https://github.com/daquexian/onnx-simplifier/issues/178

    output_nms_with_dynamic_tensor: Optional[bool]
      The number of bounding boxes in the NMS output results is
      not fixed at the maximum number of max_output_boxes_per_class,
      but rather at the smallest possible number of dynamic tensors.
      If this option is disabled, NMS output is padded to the number
      set in the max_output_boxes_per_class attribute.
      e.g.
      disable --output_nms_with_dynamic_tensor:
          output_tensor_shape: [100, 7]
      enable --output_nms_with_dynamic_tensor:
          output_tensor_shape: [N, 7]

    keep_ncw_or_nchw_or_ncdhw_input_names: Optional[List[str]]
      Holds the NCW or NCHW or NCDHW of the input shape for the specified INPUT OP names.
      If a nonexistent INPUT OP name is specified, it is ignored.
      Valid only for 3D, 4D and 5D input tensors.
      e.g.
      keep_ncw_or_nchw_or_ncdhw_input_names=['input0','input1','input2']

    keep_nwc_or_nhwc_or_ndhwc_input_names: Optional[List[str]]
      Holds the NWC or NHWC or NDHWC of the input shape for the specified INPUT OP names.
      If a nonexistent INPUT OP name is specified, it is ignored.
      If the input OP name is the same as the input OP name specified
      in the keep_ncw_or_nchw_or_ncdhw_input_names option, it is ignored.
      Valid only for 3D, 4D and 5D input tensors.
      e.g.
      keep_nwc_or_nhwc_or_ndhwc_input_names=['input0','input1','input2']

    keep_shape_absolutely_input_names: Optional[List[str]]
      Name of the INPUT that unconditionally maintains its shape.
      If a nonexistent INPUT OP name is specified, it is ignored.
      e.g.
      keep_shape_absolutely_input_names=['input0','input1','input2']

    output_names_to_interrupt_model_conversion: Optional[List[str]]
      Output names of ONNX that interrupt model conversion.
      Interrupts model transformation at the specified output name
      and outputs the model partitioned into subgraphs.
      e.g.
      output_names_to_interrupt_model_conversion=['output0','output1','output2']

    disable_group_convolution: Optional[bool]
      Disable GroupConvolution and replace it with SeparableConvolution for
      output to saved_model format.

    enable_batchmatmul_unfold: Optional[bool]
      BatchMatMul is separated batch by batch to generate a primitive MatMul.

    enable_rnn_unroll: Optional[bool]
      Instead of increasing inference speed by expanding all symbolic loops of
      the RNN (LSTM, GRU, RNN), RAM consumption will increase because all tensors
      are expanded and embedded in the model.
      https://keras.io/api/layers/recurrent_layers/

    disable_suppression_flextranspose: Optional[bool]
      Disables FlexTranspose generation suppression.

    number_of_dimensions_after_flextranspose_compression: Optional[int]
      Number of Transpose OP dimensions generated after avoiding FlexTranspose generation.
      Also suppress the creation of the Transpose itself by specifying 2.
      Default: 6

    disable_suppression_flexstridedslice: Optional[bool]
      Disables FlexStridedSlice generation suppression.

    disable_strict_mode: Optional[bool]
      If specified, the conversion speed is greatly accelerated because the strict accuracy
      correction process is skipped, but the frequency of transposition errors increases
      and accuracy errors are more likely to occur. Strict mode is enabled by default.
      As of 2023.05.07, this is a work in progress and is an experimental feature.
      Therefore, only some OPs are converted in strict mode for accuracy correction.

    number_of_dimensions_after_flexstridedslice_compression: Optional[int]
      Number of StridedSlice OP dimensions generated after avoiding FlexStridedSlice generation.
      Default: 5

    optimization_for_gpu_delegate: Optional[bool]
      Replace operations that do not support gpu delegate with those
      that do as much as possible.

    replace_argmax_to_reducemax_and_indicies_is_int64: Optional[bool]
      Replace ArgMax with a ReduceMax. The returned indicies are int64.
      Only one of replace_argmax_to_reducemax_and_indicies_is_int64 and
      replace_argmax_to_reducemax_and_indicies_is_float32 and
      replace_argmax_to_fused_argmax_and_indicies_is_int64 and
      replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.
      Default: False

    replace_argmax_to_reducemax_and_indicies_is_float32: Optional[bool]
      Replace ArgMax with a ReduceMax. The returned indicies are float32.
      Only one of replace_argmax_to_reducemax_and_indicies_is_int64 and
      replace_argmax_to_reducemax_and_indicies_is_float32 and
      replace_argmax_to_fused_argmax_and_indicies_is_int64 and
      replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.
      Default: False

    replace_argmax_to_fused_argmax_and_indicies_is_int64: Optional[bool]
      Replace ArgMax with a ReduceMax. The returned indicies are int64.
      It improves inference speed at the cost of a small sacrifice in accuracy.
      See. https://github.com/tensorflow/models/tree/master/official/projects/edgetpu/vision#argmax-fusion-to-improve-segmentation-model-latency
      Currently, only 4D tensors are supported.
      Only one of replace_argmax_to_reducemax_and_indicies_is_int64 and
      replace_argmax_to_reducemax_and_indicies_is_float32 and
      replace_argmax_to_fused_argmax_and_indicies_is_int64 and
      replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.
      Default: False

    replace_argmax_to_fused_argmax_and_indicies_is_float32: Optional[bool]
      Replace ArgMax with a ReduceMax. The returned indicies are float32.
      It improves inference speed at the cost of a small sacrifice in accuracy.
      See. https://github.com/tensorflow/models/tree/master/official/projects/edgetpu/vision#argmax-fusion-to-improve-segmentation-model-latency
      Currently, only 4D tensors are supported.
      Only one of replace_argmax_to_reducemax_and_indicies_is_int64 and
      replace_argmax_to_reducemax_and_indicies_is_float32 and
      replace_argmax_to_fused_argmax_and_indicies_is_int64 and
      replace_argmax_to_fused_argmax_and_indicies_is_float32 can be specified.
      Default: False

    fused_argmax_scale_ratio: Optional[float]
      For Fused ArgMax.
      Scale ratio when generating Fused ArgMax.
      0.0 < fused_argmax_scale_ratio <= 1.0
      Default: 0.5

    replace_to_pseudo_operators: List[str]
      Replace list of operators to pseudo operators.
      Full name of the target operators should be given.
      Currently supported operators :
      Asin, Acos, Atan, Abs, PReLU, LeakyReLU, Power, GatherND, Neg, HardSwish, Erf

    mvn_epsilon: Optional[float]
      For MeanVarianceNormalization.
      The number to be added to the variance to avoid division by zero
      when normalizing the value.
      (input_tensor - mean) / tf.sqrt(variance + mvn_epsilon)
      Default: 0.0000000001

    param_replacement_file: Optional[str]
      Parameter replacement file path. (.json)

    check_gpu_delegate_compatibility: Optional[bool]
      Run TFLite ModelAnalyzer on the generated Float16 tflite model
      to check if the model can be supported by GPU Delegate.
      e.g.
      """
      === TFLite ModelAnalyzer ===

      Your TFLite model has '1' subgraph(s). In the subgraph description below,
      T# represents the Tensor numbers. For example, in Subgraph#0, the RESHAPE op takes
      tensor #0 and tensor #6 as input and produces tensor #7 as output.

      Subgraph#0 main(T#0) -> [T#17]
        Op#0 RESHAPE(T#0, T#6[2, 8, 8, 3, 2, ...]) -> [T#7]
        Op#1 SPLIT(T#5[0], T#7) -> [T#8, T#9]
        Op#2 RESHAPE(T#8, T#1[8, 8, 3, 2, 2]) -> [T#10]
        Op#3 TRANSPOSE(T#10, T#4[0, 3, 1, 4, 2]) -> [T#11]
        Op#4 RESHAPE(T#11, T#2[1, 8, 2, 8, 2, ...]) -> [T#12]
        Op#5 RESHAPE(T#9, T#1[8, 8, 3, 2, 2]) -> [T#13]
        Op#6 TRANSPOSE(T#13, T#4[0, 3, 1, 4, 2]) -> [T#14]
        Op#7 RESHAPE(T#14, T#2[1, 8, 2, 8, 2, ...]) -> [T#15]
        Op#8 CONCATENATION(T#12, T#15) -> [T#16]
        Op#9 RESHAPE(T#16, T#3[2, 16, 16, 3]) -> [T#17]

      Tensors of Subgraph#0
        T#0(inputs_0) shape:[2, 8, 8, 12], type:FLOAT32
        T#1(model/tf.compat.v1.squeeze_2/Squeeze) shape:[5], type:INT32 RO 20 bytes, data:[8, 8, 3, 2, 2]
        T#2(model/tf.expand_dims_1/ExpandDims) shape:[6], type:INT32 RO 24 bytes, data:[1, 8, 2, 8, 2, ...]
        T#3(model/tf.reshape_1/Reshape/shape) shape:[4], type:INT32 RO 16 bytes, data:[2, 16, 16, 3]
        T#4(model/tf.compat.v1.transpose/transpose/perm) shape:[5], type:INT32 RO 20 bytes, data:[0, 3, 1, 4, 2]
        T#5(model/tf.concat/concat/axis) shape:[], type:INT32 RO 4 bytes, data:[0]
        T#6(model/tf.reshape/Reshape/shape) shape:[6], type:INT32 RO 24 bytes, data:[2, 8, 8, 3, 2, ...]
        T#7(model/tf.reshape/Reshape) shape:[2, 8, 8, 3, 2, 2], type:FLOAT32
        T#8(model/tf.split/split) shape:[1, 8, 8, 3, 2, 2], type:FLOAT32
        T#9(model/tf.split/split1) shape:[1, 8, 8, 3, 2, 2], type:FLOAT32
        T#10(model/tf.compat.v1.squeeze_1/Squeeze) shape:[8, 8, 3, 2, 2], type:FLOAT32
        T#11(model/tf.compat.v1.transpose/transpose) shape:[8, 2, 8, 2, 3], type:FLOAT32
        T#12(model/tf.expand_dims/ExpandDims) shape:[1, 8, 2, 8, 2, 3], type:FLOAT32
        T#13(model/tf.compat.v1.squeeze_2/Squeeze1) shape:[8, 8, 3, 2, 2], type:FLOAT32
        T#14(model/tf.compat.v1.transpose_1/transpose) shape:[8, 2, 8, 2, 3], type:FLOAT32
        T#15(model/tf.expand_dims_1/ExpandDims1) shape:[1, 8, 2, 8, 2, 3], type:FLOAT32
        T#16(model/tf.concat/concat) shape:[2, 8, 2, 8, 2, 3], type:FLOAT32
        T#17(Identity) shape:[2, 16, 16, 3], type:FLOAT32

      Your model looks compatibile with GPU delegate with TFLite runtime version 2.10.0.
      But it doesn't guarantee that your model works well with GPU delegate.
      There could be some runtime incompatibililty happen.
      ---------------------------------------------------------------
                    Model size:       2988 bytes
          Non-data buffer size:       2757 bytes (92.27 %)
        Total data buffer size:        231 bytes (07.73 %)
          (Zero value buffers):          4 bytes (00.13 %)

      * Buffers of TFLite model are mostly used for constant tensors.
        And zero value buffers are buffers filled with zeros.
        Non-data buffers area are used to store operators, subgraphs and etc.
        You can find more details from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema.fbs
      """

    check_onnx_tf_outputs_elementwise_close: Optional[bool]
      Returns "Matches" if the output of onnx and the output of TF are
      within acceptable proximity element by element.
      Returns "Unmatched" if the output of onnx and the output of TF are
      not within acceptable proximity element by element.
      If the output of onnx is 1D, it returns "Skipped" and skips the comparison
      between the output of onnx and that of TF. This is because when undefined
      dimensions are present, a situation often arises where very large index
      values are compared, causing OutOfMemory.
      Only the output content of the models final output OP is checked.

    check_onnx_tf_outputs_elementwise_close_full: Optional[bool]
      Returns "Matches" if the output of onnx and the output of TF are
      within acceptable proximity element by element.
      Check the output of all OPs in sequence from the beginning,
      including all but the final output OP of the model.
      Returns "Unmatched" if the output of onnx and the output of TF are
      not within acceptable proximity element by element.
      If the output of onnx is 1D, it returns "Skipped" and skips the comparison
      between the output of onnx and that of TF. This is because when undefined
      dimensions are present, a situation often arises where very large index
      values are compared, causing OutOfMemory.
      It is very time consuming because it performs as many inferences as
      there are operations.

    check_onnx_tf_outputs_sample_data_normalization: Optional[str]
      norm: Validate using random data normalized to the range 0.0 to 1.0
      denorm: Validate using random data in the range 0.0 to 255.0
      If there is a normalization layer at the models entry point, or
      if the model was trained on denormalized data, "denorm" must be specified.
      Default: "norm"

    check_onnx_tf_outputs_elementwise_close_rtol: Optional[float]
      The relative tolerance parameter.
      Default: 0.0

    check_onnx_tf_outputs_elementwise_close_atol: Optional[float]
      The absolute tolerance parameter.
      Default: 1e-4

    disable_model_save: Optional[bool]
      Does not save the converted model. For CIs RAM savings.
      Default: False

    use_cuda: Optional[bool]
      CUDA is used for dummy inference during accuracy checks,
      but accuracy is degraded.
      Note that if you need to convert extended OPs such as com.microsoft.xxx,
      you must enable this flag.
      Default: False

    non_verbose: Optional[bool]
      Shorthand to specify a verbosity of "error".
      Default: False

    verbosity: Optional[str]
      Change the level of information printed.
      Values are "debug", "info", "warn", and "error".
      Default: "debug" (for backwards compatability)

    Returns
    ----------
    model: tf.keras.Model
      Model
```

## Parameter replacement
This tool is used to convert `NCW` to `NWC`, `NCHW` to `NHWC`, `NCDHW` to `NDHWC`, `NCDDHW` to `NDDHWC`, `NCDDDDDDHW` to `NDDDDDDHWC`. Therefore, as stated in the Key Concepts, the conversion will inevitably break down at some point in the model. You need to look at the entire conversion log to see which OP transpositions are failing and correct them yourself. I dare to explain very little because I know that no matter how much detail I put in the README, you guys will not read it at all. `attribute` or `INPUT constant` or `INPUT Initializer` can be replaced with the specified value.

Starting from `v1.3.0`, almost all OPs except for some special OPs support pre- and post-transposition by `pre_process_transpose` and `post_process_transpose`.

1. "A conversion error occurs."
2. "Output results are wrong."

Do not submit an issue that only contains an amount of information that cannot be reproduced.

- convert option
  ```
  --param_replacement_file param_replacement.json

  or

  -prf param_replacement.json
  ```

- param_replacement.json

  <details><summary>See a sample of replacement JSON</summary><div>

  ```yaml
  {
    "format_version": 1,
    "operations": [
      {
        "op_name": "StatefulPartitionedCall/Tile_4",
        "param_target": "inputs", # attributes or inputs
        "param_name": "const_fold_opt__677",
        "values": [1,1,17] # Disable parameter transposition or overwrite parameters
      },
      {
        "op_name": "StatefulPartitionedCall/Cast_3",
        "param_target": "attributes", # attributes or inputs
        "param_name": "to",
        "values": 1 # Disable parameter transposition or overwrite "to" parameters
      },
      {
        "op_name": "Resize__697",
        "param_target": "inputs",
        "param_name": "Concat__696:0",
        "values": [26,26] # Replacement of unk__x (Resize OP, sizes height/width parameter)
      },
      {
        "op_name": "Transpose__927",
        "param_target": "attributes",
        "param_name": "perm",
        "values": [0,1,2,3] # Disable parameter transposition or overwrite "perm" parameters
      },
      {
        "op_name": "StatefulPartitionedCall/functional_1/max_unpooling2d_2/Reshape_1",
        "param_target": "inputs",
        "param_name": "const_fold_opt__911",
        "values": [4,131072] # Overwrite "shape" parameters
      },
      {
        "op_name": "Reshape_25",
        "param_target": "outputs",
        "param_name": "onnx::InstanceNormalization_270",
        "post_process_transpose_perm": [0,2,1] # Extrapolate 3D Transpose after Reshape
      },
      {
        "op_name": "Reshape_30",
        "param_target": "outputs",
        "param_name": "onnx::Mul_275",
        "post_process_transpose_perm": [0,2,3,1] # Extrapolate 4D Transpose after Reshape
      },
      {
        "op_name": "flatten_1127",
        "param_target": "inputs",
        "param_name": "dropout0",
        "pre_process_transpose_perm": [0,3,1,2]
      },
      {
        "op_name": "/Slice",
        "param_target": "op",
        "begin": [0,0,1,0],
        "end": [0,0,0,0],
        "end_mask": 15
      },
      {
        "op_name": "/Slice_1",
        "param_target": "op",
        "begin": [0,0,0,0],
        "end": [0,0,39,0],
        "end_mask": 11
      },
      {
        "op_name": "/backbone/backbone.1/Unsqueeze_1",
        "param_target": "op",
        "new_shape": [1,15,15,1]
      }
    ]
  }
  ```

  </div></details>

- Replacement Supported OPs

  <details><summary>See list of replacement specifications</summary><div>

  |No.|OP type|Remarks|
  |:-:|:-|:-|
  |1|Add|1. "param_target": "inputs"<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Add operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Add operation with the perm specified as post-processing.|
  |2|Cast|<table><thead><th>Type</th><th align="right">Values</th><th>Type</th><th align="right">Values</th></thead><tbody><tr><td>float16</td><td align="right">10</td><td>int8</td><td align="right">3</td></tr><tr><td>float32</td><td align="right">1</td><td>int16</td><td align="right">5</td></tr><tr><td>float64</td><td align="right">11</td><td>int32</td><td align="right">6</td></tr><tr><td>bool</td><td align="right">9</td><td>int64</td><td align="right">7</td></tr><tr><td>uint8</td><td align="right">2</td><td colspan="2" rowspan="4"></td></tr><tr><td>uint16</td><td align="right">4</td></tr><tr><td>uint32</td><td align="right">12</td></tr><tr><td>uint64</td><td align="right">13</td></tr></tbody></table>|
  |3|Concat|1. "param_target": "attributes"<br>`axis`: Value of `axis`<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Concat operation with the perm specified as post-processing.|
  |4|ConvTranspose|`ConvTranspose` implements special replacements separately ignore all automatic conversions and generate `tf.nn.conv1d_transpose` or `tf.nn.conv2d_transpose` or `tf.nn.conv3d_transpose` directly by specifying all parameters.<br>https://www.tensorflow.org/api_docs/python/tf/nn/conv1d_transpose<br>https://www.tensorflow.org/api_docs/python/tf/nn/conv2d_transpose<br>https://www.tensorflow.org/api_docs/python/tf/nn/conv3d_transpose<br>1. "param_target": "op"<br>`output_shape`: Value of `output_shape`<br>`strides`: Value of `strides`<br>`padding`: Value of `padding`<br>`dilations`: Value of `dilations`|
  |5|Div|1. "param_target": "inputs"<br>`values`: Value of `input`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Div operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Div operation with the perm specified as post-processing.|
  |6|Expand|1. "param_target": "inputs"<br>`values`: Value of `shape`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Expand operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Expand operation with the perm specified as post-processing.|
  |7|Flatten|1. "param_target": "attributes"<br>`axis`: Value of `axis`<br>2. "param_target": "inputs"<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Flatten operation with the perm specified as pre-processing.<br>3. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Flatten operation with the perm specified as post-processing.|
  |8|Gemm||
  |9|Gather|1. "param_target": "attributes"<br>`axis`: Value of `axis`<br>2. "param_target": "inputs"<br>`values`: Value of `indices`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Gather operation with the perm specified as pre-processing.<br>3. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Gather operation with the perm specified as post-processing.|
  |10|MatMul|1. "param_target": "inputs"<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the MatMul operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the MatMul operation with the perm specified as post-processing.|
  |11|Mul|1. "param_target": "inputs"<br>`values`: Value of `input`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Mul operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Mul operation with the perm specified as post-processing.|
  |12|NonMaxSuppression||
  |13|ReduceL1<br>ReduceL2<br>ReduceLogSum<br>ReduceLogSumExp<br>ReduceMax<br>ReduceMean<br>ReduceMin<br>ReduceProd<br>ReduceSum<br>ReduceSumSquare|1. "param_target": "attributes"<br>`axes`: Value of `axes`<br>`keepdims`: Value of `keepdims`<br>2. "param_target": "inputs"<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the ReduceXX operation with the perm specified as pre-processing.<br>3. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the ReduceXX operation with the perm specified as post-processing.|
  |14|Unsqueeze|1. "param_target": "inputs"<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Unsqueeze operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Unsqueeze operation with the perm specified as post-processing.<br>3. "param_target": "op"<br>`new_shape`: Specifies directly the shape after Unsqueeze processing.<br>{<br>&nbsp;&nbsp;"op_name": "/backbone/backbone.1/Unsqueeze_1",<br>&nbsp;&nbsp;"param_target": "op",<br>&nbsp;&nbsp;"new_shape": [1,15,15,1]<br>}|
  |15|Reshape|1. "param_target": "inputs"<br>`values`: Value of `shape`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Reshape operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Reshape operation with the perm specified as post-processing.|
  |16|Resize|1. "param_target": "attributes"<br>`coordinate_transformation_mode`: Value of `coordinate_transformation_mode`<br>`extrapolation_value`: Value of `extrapolation_value`<br>`mode`: Value of `mode`<br>2. "param_target": "inputs"<br>`values`: Value of `roi` or `scales` or `sizes`. `scales`=`[scale_h,scale_w]`,`sizes`=`[h,w]`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Resize operation with the perm specified as pre-processing.<br>3. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Resize operation with the perm specified as post-processing.|
  |17|Slice|`Slice` implements special replacements separately ignore all automatic conversions and generate `tf.strided_slice` directly by specifying all parameters of `tf.strided_slice` directly.<br>https://www.tensorflow.org/api_docs/python/tf/strided_slice<br>See [replace_slice.json](https://github.com/PINTO0309/onnx2tf/blob/main/replace_slice.json) for a sample description.<br>![20221221222956](https://user-images.githubusercontent.com/33194443/208916732-9987a69a-83a7-4a29-8b77-d97b1812d59c.png)<br>1. "param_target": "op"<br>`begin`: Value of `begin`<br>`end`: Value of `end`<br>`strides`: Value of `strides`<br>`begin_mask`: Value of `begin_mask`<br>`end_mask`: Value of `end_mask`<br>`ellipsis_mask`: Value of `ellipsis_mask`<br>`new_axis_mask`: Value of `new_axis_mask`<br>`shrink_axis_mask`: Value of `shrink_axis_mask`<br>{<br>&nbsp;&nbsp;"op_name": "/Slice",<br>&nbsp;&nbsp;"param_target": "op",<br>&nbsp;&nbsp;"begin": [0,0,1,0],<br>&nbsp;&nbsp;"end": [0,0,0,0],<br>&nbsp;&nbsp;"end_mask": 15<br>}|
  |18|Softmax|1. "param_target": "attributes"<br>`axis`: Value of `axis`. The transpositions corresponding to the specified axis are extrapolated before and after `Softmax`.<br>2. "param_target": "inputs"<br>`values`: Value of `tensor`|
  |19|Split|1. "param_target": "inputs"<br>`values`: Value of `split`<br>2. "param_target": "attributes"<br>`axis`: Value of `axis`.<br>`num_outputs`: Value of `num_outputs`.|
  |20|Sub|1. "param_target": "inputs"<br>`values`: Value of `input`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Sub operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Sub operation with the perm specified as post-processing.|
  |21|Tile|1. "param_target": "inputs"<br>`values`: Value of `input`<br>`pre_process_transpose_perm`: Transpose is applied to the tensor before the Tile operation with the perm specified as pre-processing.<br>2. "param_target": "outputs"<br>`post_process_transpose_perm`: Transpose is applied to the tensor after the Tile operation with the perm specified as post-processing.|
  |22|Transpose|1. "param_target": "attributes"<br>`perm`: Value of `perm`<br>2. "param_target": "inputs"<br>`values`: Value of `tensor`|

  </div></details>

## Generated Model
- YOLOv7-tiny with Post-Process (NMS) ONNX to TFLite Float32
  https://github.com/PINTO0309/onnx2tf/releases/download/0.0.33/yolov7_tiny_head_0.768_post_480x640.onnx

  <details><summary>See the structure of the model</summary><div>

  |onnx2tf|onnx-tensorflow<br>(Super redundant + Broken)|
  |:-:|:-:|
  |![image](https://user-images.githubusercontent.com/33194443/198160732-47ef9770-ecca-40dd-8502-be41c941f8e3.png)|![image](https://user-images.githubusercontent.com/33194443/195248761-9d4f4446-3fb4-41ad-a5d4-a7d211b527c0.png)|

  </div></details>

- YOLACT-Edge MobileNetV2 with Post-Process (MultiClass-NMS) ONNX to TFLite Float32
  https://github.com/PINTO0309/onnx2tf/releases/download/1.0.11/yolact_edge_mobilenetv2_550x550.onnx

  <details><summary>See the structure of the model</summary><div>

  ![image](https://user-images.githubusercontent.com/33194443/201506248-6ee1e04d-3b5a-4afb-a05c-bf8d5119297b.png)

  </div></details>

- MoveNet MultiPose ONNX to TFLite Float32 (`Cast` and `TrueDiv` standard OP support)
  https://github.com/PINTO0309/onnx2tf/releases/download/1.0.24/movenet_multipose_lightning_192x256_p6.onnx

  <details><summary>See the structure of the model</summary><div>

  ![image](https://user-images.githubusercontent.com/33194443/198175219-b2db3ba3-65f8-464c-a0fd-411c4a62402e.png)

  </div></details>

## Validated models (without replacement.json)
ONNX file for testing. https://github.com/PINTO0309/onnx2tf/releases/tag/1.1.28

<details><summary>See a list of verified models</summary><div>

|No.|Model|Pass|
|:-:|:-|:-:|
|1|age_googlenet.onnx|:heavy_check_mark:|
|2|alike_t_opset11_192x320.onnx|:heavy_check_mark:|
|3|arcfaceresnet100-8.onnx|:heavy_check_mark:|
|4|baseline_simplified.onnx|:heavy_check_mark:|
|5|big_slice_11.onnx|:heavy_check_mark:|
|6|bvlcalexnet-12.onnx|:heavy_check_mark:|
|7|caffenet-12.onnx|:heavy_check_mark:|
|8|convtranspose_3_1_5_2.onnx|:heavy_check_mark:|
|9|convtranspose_4_5_2_2.onnx|:heavy_check_mark:|
|10|convtranspose_5_5_6_1.onnx|:heavy_check_mark:|
|11|convtranspose_6_5_5_8.onnx|:heavy_check_mark:|
|12|convtranspose_7_1_3_4.onnx|:heavy_check_mark:|
|13|damoyolo_tinynasL20_T_192x192_post.onnx|:heavy_check_mark:|
|14|deeplabv3_mobilenet_v3_large.onnx|:heavy_check_mark:|
|15|densenet-12.onnx|:heavy_check_mark:|
|16|depth_to_spase_17.onnx|:heavy_check_mark:|
|17|double_gru.onnx|:heavy_check_mark:|
|18|digits.onnx|:heavy_check_mark:|
|19|detr_demo.onnx|:heavy_check_mark:|
|20|efficientformer_l1.onnx|:heavy_check_mark:|
|21|efficientdet_lite2_detection_1.onnx|:heavy_check_mark:|
|22|efficientnet-lite4-11_nchw.onnx|:heavy_check_mark:|
|23|effnet_opset11_dynamic_axis.onnx|:heavy_check_mark:|
|24|emotion-ferplus-8_rename.onnx|:heavy_check_mark:|
|25|face_detection_yunet_2022mar.onnx|:heavy_check_mark:|
|26|face_recognition_sface_2021dec-act_int8-wt_int8-quantized.onnx|:heavy_check_mark:|
|27|face_recognition_sface_2021dec.onnx|:heavy_check_mark:|
|28|faster_rcnn-10.onnx|:heavy_check_mark:|
|29|fastestdet.onnx|:heavy_check_mark:|
|30|fused_conv_clip.onnx|:heavy_check_mark:|
|31|fused_conv_hardsigmoid.onnx|:heavy_check_mark:|
|32|fused_conv_leakyrelu.onnx|:heavy_check_mark:|
|33|fused_conv_relu.onnx|:heavy_check_mark:|
|34|fused_conv_sigmoid.onnx|:heavy_check_mark:|
|35|fused_conv_tanh.onnx|:heavy_check_mark:|
|36|gender_googlenet.onnx|:heavy_check_mark:|
|37|gmflow-scale1-mixdata-train320x576-4c3a6e9a_1x3x480x640_bidir_flow_sim.onnx|:heavy_check_mark:|
|38|handpose_estimation_mediapipe_2022may.onnx|:heavy_check_mark:|
|39|htnet_1x17x2_without_norm.onnx|:heavy_check_mark:|
|40|iat_llie_180x320.onnx|:heavy_check_mark:|
|41|if_p1_11.onnx|:heavy_check_mark:|
|42|if_p2_11.onnx|:heavy_check_mark:|
|43|if_p3_11.onnx|:heavy_check_mark:|
|44|imageclassifier.onnx|:heavy_check_mark:|
|45|inception-v2-9.onnx|:heavy_check_mark:|
|46|inverse11.onnx|:heavy_check_mark:|
|47|mhformer_NxFxKxXY_1x27x17x2.onnx|:heavy_check_mark:|
|48|mnist.onnx|:heavy_check_mark:|
|49|mnist-12.onnx|:heavy_check_mark:|
|50|mobilenetv2-12.onnx|:heavy_check_mark:|
|51|mosaic_11.onnx|:heavy_check_mark:|
|52|mosaic-9.onnx|:heavy_check_mark:|
|53|movenet_multipose_lightning_192x256_p6.onnx|:heavy_check_mark:|
|54|nanodet-plus-m_416.onnx|:heavy_check_mark:|
|55|object_tracking_dasiamrpn_kernel_cls1_2021nov.onnx|:heavy_check_mark:|
|56|object_tracking_dasiamrpn_kernel_r1_2021nov.onnx|:heavy_check_mark:|
|57|object_tracking_dasiamrpn_model_2021nov.onnx|:heavy_check_mark:|
|58|pidnet_S_cityscapes_192x320.onnx|:heavy_check_mark:|
|59|ppmattingv2_stdc1_human_480x640.onnx|:heavy_check_mark:|
|60|qlinear_conv_tensor_test.onnx|:heavy_check_mark:|
|61|rcnn-ilsvrc13-9.onnx|:heavy_check_mark:|
|62|regnet_x_400mf.onnx|:heavy_check_mark:|
|63|ResNet101-DUC-12.onnx|:heavy_check_mark:|
|64|resnet18-v1-7.onnx|:heavy_check_mark:|
|65|resnet50-v1-12.onnx|:heavy_check_mark:|
|66|resnet50-v2-7.onnx|:heavy_check_mark:|
|67|retinanet-9.onnx|:heavy_check_mark:|
|68|sinet_320_op.onnx|:heavy_check_mark:|
|69|squeezenet1.0-12.onnx|:heavy_check_mark:|
|70|super-resolution-10.onnx|:heavy_check_mark:|
|71|swinir-m_64x64_12.onnx|:heavy_check_mark:|
|72|text_recognition_CRNN_EN_2021sep.onnx|:heavy_check_mark:|
|73|tinyyolov2-8.onnx|:heavy_check_mark:|
|74|version-RFB-640.onnx|:heavy_check_mark:|
|75|vit-b-32_textual.onnx|:heavy_check_mark:|
|76|vit-b-32_visual.onnx|:heavy_check_mark:|
|77|yolact_edge_mobilenetv2_550x550.onnx|:heavy_check_mark:|
|78|yolact_regnetx_600mf_d2s_31classes_512x512.onnx|:heavy_check_mark:|
|79|yolact_regnetx_800mf_20classes_512x512.onnx|:heavy_check_mark:|
|80|yolo_free_nano_crowdhuman_192x320_post.onnx|:heavy_check_mark:|
|81|yolov7_tiny_head_0.768_post_480x640.onnx|:heavy_check_mark:|
|82|yolov8n.onnx|:heavy_check_mark:|
|83|yolov8n-seg.onnx|:heavy_check_mark:|
|84|yolox_nano_192x192.onnx|:heavy_check_mark:|
|85|yolox_nano_416x416.onnx|:heavy_check_mark:|
|86|yolox_s.onnx|:heavy_check_mark:|
|87|yolox_x_crowdhuman_mot17_bytetrack.onnx|:heavy_check_mark:|
|88|zero_dce_640_dele.onnx|:heavy_check_mark:|
|89|zfnet512-12.onnx|:heavy_check_mark:|

</div></details>

## Key concept
- [x] [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow) is a very useful tool, but the performance of the generated TensorFlow models is significantly degraded due to the extrapolation of a large number of `Transpose` OPs before and after each OP during the format conversion from `NCHW` to `NHWC`. Therefore, I will make this tool myself as a derivative tool of [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow) without extrapolating `Transpose`.
- [x] Most of the internal processing of the tool is full-scratch, but some of the more complex OPs have been adapted from [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow). I am very grateful to the engineers at International Business Machines Corporation / LeapMind / Microsoft / IBM for developing [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow).
- [x] I have incorporated all my knowledge of model optimization to other models such as TFLite, EdgeTPU, TensorFlow.js and Myriad based on my years of experience implementing [openvino2tensorflow](https://github.com/PINTO0309/openvino2tensorflow) and [tflite2tensorflow](https://github.com/PINTO0309/tflite2tensorflow). It probably has the best model optimization performance and conversion efficiency of any tool I have created in the past, and the lowest rate of conversion errors.
- [x] Supported layers list. [Supported layers](#supported-layers)
- [x] If you are having trouble with conversion errors, searching for [resolved or open issues](https://github.com/PINTO0309/onnx2tf/issues) will almost always solve your problems. Issues are knowledge for engineers around the world.
- [x] Contributors to this repository should first read **[Contribution Guide](https://github.com/PINTO0309/onnx2tf/blob/main/CONTRIBUTING.md)**.

  https://user-images.githubusercontent.com/33194443/197319770-e7ef7174-66cd-4bc2-84be-59e1a251151d.mp4

- [x] All OPs are decomposed into primitive operations as much as possible. This is beneficial for lateral deployment of models to frameworks other than TFLite. Therefore, OPs belonging to `tf.keras.layers` are almost never used, and the tool consists only of `tf.xxx`. (except for a very few OPs)
- [x] As I do not want to add more dependent packages, I do not use `tensorflow_addons (tfa)`, but replace it with the standard OP of tensorflow.
- [x] Not only does it handle conversions of 4-dimensional inputs, such as `NCHW` to `NHWC`, but also the number of input dimensions in 3, 5, or even more dimensions. For example, `NCDHW` to `NDHWC`, etc. However, since 1-D, 2-D, 3-D and 6-D input may produce patterns that are mechanically difficult to convert, it should be possible to give parameters to externally modify the tool's behavior. See [Parameter replacement](#parameter-replacement)
- [x] If there are undefined dimensions in the input OP, the model structure is not fully optimized and conversion errors are very likely to occur.
- [x] Immediately following a `Reshape` OP with dimensional compression and dimensional decompression, there is a 95% probability that the model transformation operation will be disrupted and errors will occur. For example, patterns such as `[1,200,200,5]` -> `[1,200,-1]` or `[10,20,30,40,50]` -> `[10,2,10,30,10,4,50]` or `Flatten`. See [#8 Not able to reshape input in replace.json](https://github.com/PINTO0309/onnx2tf/issues/8), or [#15 Conv layer shape wrong](https://github.com/PINTO0309/onnx2tf/issues/15), or [#18 Question about channel_transpose in common_functions.py](https://github.com/PINTO0309/onnx2tf/issues/18), or [#105 [MobileFormer]Converted model outputs values mismatch with original ones.](https://github.com/PINTO0309/onnx2tf/issues/105), or [#133 When Onnx Matmul inputs have different dimension](https://github.com/PINTO0309/onnx2tf/issues/133).
- [x] TensorFlow's Convolution does not have an equivalent operation to ONNX's Padding operation. Therefore, a `Pad` OP is inserted immediately before a Convolution with Padding of size greater than 1.
- [x] Support conversion to TensorFlow saved model and TFLite (Float32/Float16/INT8).
- [x] Files exceeding the Protocol Buffers file size limit of 2GB are not supported. Therefore, the external format is not supported at the initial stage of tool creation.
- [x] If there are ONNX OPs that are not supported by TensorFlow, use [simple-onnx-processing-tools](https://github.com/PINTO0309/simple-onnx-processing-tools) to replace them with harmless OPs in advance and then use this tool to convert them. In other words, you can convert any model with your efforts.
- [x] ONNX splitting, merging, generating OPs, rewriting OP attributes, BGR<->RGB conversion, converting to JSON and editing in the IDE, batch size changes for undefined dimensions, and various other processing can be done with the [simple-onnx-processing-tools](https://github.com/PINTO0309/simple-onnx-processing-tools). Therefore, it is recommended that models with very complex structures be converted to TFLite after modifying the structure beforehand.
- [x] `BatchNormalization` supports only inference mode.
- [x] `LayerNormalization` supports only inference mode.
- [x] Only for `opset=11` or higher
- [x] If you do not like the generated TFLite OP name, edit it using [tflite2json2tflite](https://github.com/PINTO0309/tflite2json2tflite).
- [x] The generated Keras models cannot be used for retraining. If you want to train, you must build your own model.
- [x] When converting to TensorFlow.js, CoreML, etc., please generate saved_model with the `--output_signaturedefs` option and use the generated saved_model to convert with various converters. [tensorflowjs_converter](https://github.com/tensorflow/tfjs), [coremltools](https://github.com/apple/coremltools), [edgetpu_compilier](https://coral.ai/docs/edgetpu/compiler/), etc... If this option is not enabled, saved_model records only the minimum necessary information and its size is minimized. When this option is enabled, saved_model records the maximum amount of information, and instead of being maximized in size, the output is in a format that supports conversion to other frameworks. It can also be used for serving.
- [x] There are many OPs on ONNX that do not support TFLite/EdgeTPU/TFJS/CoreML/TensorRT. Therefore, if you need to generate an EdgeTPU model, please specify `--replace_to_pseudo_operators` to convert your model. onnx2tf will attempt to replace the OP with an TFLite/EdgeTPU/TFJS/CoreML/TensorRT-compatible OP whenever possible.
- [x] The main factors that cause accuracy degradation after model conversion are as follows
1. differences in Padding specifications
2. difference in Python division specification in the process of model transformation (error due to even rounding)
3. Divide epsilon without consideration
4. deprecated TrueDivision
5. support difference of powers
6. differences in interpolation operation specifications during resizing
7. Difference in arithmetic precision supported by each operation
8. Calculation error due to scaling up or down by specifying a `scale` when resizing images

The above differences often cannot be dealt with by simply converting the model in a straightforward manner. Therefore, you need to replace the model yourself in advance with an operation that is less prone to errors.
- [x] Support for `INT8 Quantization`, `Full INT8 Quantization`, `INT8 Quantization with INT16 activation`, `Full INT8 Quantization with INT16 activation` and `Dynamic Range Quantization`.
- [x] Support for `Per-Channel Quantization` and `Per-Tensor Quantization`.
- [x] Support for `GroupConvolution`.
- [x] TFLite does not support `TrueDiv`(INT), so `TrueDiv` is avoided if possible.
- [x] Implement the `Resize` process for the 5D tensor.
- [x] Add process to replace `Asin` with `pseudo-Asin`.
- [x] Add process to replace `Acos` with `pseudo-Acos`.
- [x] Add process to replace `Atan` with `pseudo-Atan`.
- [x] Add process to replace `Abs` with `pseudo-Abs`.
- [x] Add process to replace `GatherND` with `pseudo-GatherND`.
- [x] Add process to replace `HardSwish` with `pseudo-HardSwish`.
- [x] Add process to replace `GridSample` with `pseudo-GridSample`.
- [x] Add process to replace `PRelu` with `pseudo-PRelu`.
- [x] Add process to replace `LeakyRelu` with `pseudo-LeakyRelu`.
- [x] Add process to replace `Power` with `pseudo-Power`.
- [x] Add process to replace `Neg` with `pseudo-Neg`.
- [x] Add process to replace `ArgMax` with `pseudo-ArgMax`.
- [x] Add process to replace `Erf` with `pseudo-Erf`.
- [x] Added option to fix dynamic batch size `N` to a specified number.
- [x] Added option to overwrite dynamic shape input OPs with static shape. `--overwrite_input_shape`
- [x] Output in Keras H5 format.
- [x] Automatically run [onnx-simplifier](https://github.com/daquexian/onnx-simplifier) (onnxsim) backend and optimize onnx files before model transformation.
- [x] Added the ability to automatically generate each OP name and assign OP names to ONNX files in the old format.
- [x] Supports model splitting. Interrupts model transformation at the specified output name and outputs the model partitioned into subgraphs.

## Related tools
1. [tflite2tensorflow](https://github.com/PINTO0309/tflite2tensorflow)
2. [openvino2tensorflow](https://github.com/PINTO0309/openvino2tensorflow)
3. [tflite2json2tflite](https://github.com/PINTO0309/tflite2json2tflite)
4. [tensorflowjs_converter](https://github.com/tensorflow/tfjs)
5. [coremltools](https://github.com/apple/coremltools)
6. [simple-onnx-processing-tools](https://github.com/PINTO0309/simple-onnx-processing-tools)
7. [tflite-input-output-rewriter](https://github.com/PINTO0309/tflite-input-output-rewriter)
8. [onnx-simplifier](https://github.com/daquexian/onnx-simplifier)
9. [onnx_graphsurgeon](https://github.com/NVIDIA/TensorRT/tree/master/tools/onnx-graphsurgeon)
10. [onnx](https://github.com/onnx/onnx)
11. [onnx-tensorflow](https://github.com/onnx/onnx-tensorflow)
12. [onnx2keras](https://github.com/gmalivenko/onnx2keras)
13. [TinyNeuralNetwork](https://github.com/alibaba/TinyNeuralNetwork)
14. [nobuco](https://github.com/AlexanderLutsenko/nobuco)
15. [onnx2torch](https://github.com/ENOT-AutoDL/onnx2torch)

## Acknowledgement
1. https://github.com/onnx/models
2. https://github.com/opencv/opencv_zoo
3. https://pytorch.org/vision/stable/models.html
4. https://tfhub.dev/
5. https://www.kaggle.com/models
6. https://github.com/TexasInstruments/edgeai-modelzoo

## Contributors
<a href="https://github.com/pinto0309/onnx2tf/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=pinto0309/onnx2tf" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
