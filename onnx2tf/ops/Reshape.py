import random
random.seed(0)
import numpy as np
np.random.seed(0)
import tensorflow as tf
import onnx_graphsurgeon as gs
from utils.common_functions import (
    get_constant_or_variable,
    convert_reverse_axis,
)
from utils.colors import Color


def make_node(
    *,
    graph_node: gs.Node,
    tf_layers_dict: dict,
    **kwargs: dict,
):
    """Reshape

    Parameters
    ----------
    graph_node: gs.Node
        graph_surgeon Node

    tf_layers_dict: dict
        optype, shape, dtype, tensorflow graph
    """
    graph_node_input_1 = get_constant_or_variable(graph_node.inputs[0])
    graph_node_input_2 = None
    if len(graph_node.inputs) == 2:
        graph_node_input_2 = get_constant_or_variable(graph_node.inputs[1])
    graph_node_output: gs.Variable = graph_node.outputs[0]
    shape = graph_node_output.shape
    dtype = graph_node_output.dtype

    input_tensor = tf_layers_dict[graph_node_input_1.name]['tf_node'] \
        if isinstance(graph_node_input_1, gs.Variable) else graph_node_input_1
    tensor_rank = len(input_tensor.shape)

    reshape_shape = tf_layers_dict[graph_node_input_2.name]['tf_node'] \
        if isinstance(graph_node_input_2, gs.Variable) else graph_node_input_2
    if reshape_shape is not None and reshape_shape.shape is None:
        reshape_shape = []
    if reshape_shape is None:
        reshape_shape = []

    allowzero = bool(graph_node.attrs.get('allowzero', 0))
    if allowzero:
        error_msg = f'' +\
            f'{Color.RED}ERROR:{Color.RESET} ' +\
            f'TensorFlow does not support allowzero=1 (True).'
        print(error_msg)
        assert not allowzero, error_msg

    # Preserving Graph Structure (Dict)
    tf_layers_dict[graph_node_output.name] = {
        'optype': graph_node.op,
        'shape': shape,
        'dtype': dtype,
    }

    # Generation of TF OP
    # NWC->NCW, NHWC->NCHW, NDHWC->NCDHW Transpose
    perm = [convert_reverse_axis(axis=idx, tensor_rank=tensor_rank) for idx in range(tensor_rank)]
    transposed_tensor = tf.transpose(
        a=input_tensor,
        perm=list(perm) if perm is not None else None,
    )
    # Reshape
    tf_layers_dict[graph_node_output.name]['tf_node'] = \
        tf.reshape(
            tensor=transposed_tensor,
            shape=reshape_shape,
            name=graph_node.name,
        )