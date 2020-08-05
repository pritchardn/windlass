from Experiments import droputils
from ..drop import BarrierAppDROP, ContainerDROP
from ..meta import dlg_float_param, dlg_component, dlg_batch_input, \
    dlg_batch_output, dlg_streaming_input


class CopyApp(BarrierAppDROP):
    """
    A BarrierAppDrop that copies its inputs into its outputs.
    All inputs are copied into all outputs in the order they were declared in
    the graph.
    """
    compontent_meta = dlg_component('CopyApp', 'Copy App.',
                                    [dlg_batch_input('binary/*', [])],
                                    [dlg_batch_output('binary/*', [])],
                                    [dlg_streaming_input('binary/*')])

    def run(self):
        self.copyAll()

    def copyAll(self):
        for inputDrop in self.inputs:
            self.copyRecursive(inputDrop)

    def copyRecursive(self, inputDrop):
        if isinstance(inputDrop, ContainerDROP):
            for child in inputDrop.children:
                self.copyRecursive(child)
        else:
            for outputDrop in self.outputs:
                droputils.copyDropContents(inputDrop, outputDrop)