from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP, InMemoryDROP, BarrierAppDROP
from dlg.droputils import allDropContents
import time
import os
from six import BytesIO

output_fname = os.getcwd() + '/result2.out'

class PrependResult(BarrierAppDROP):
    def dataURL(self):
        pass

    def initialize(self, **kwargs):
        super(PrependResult, self).initialize(**kwargs)
        self.prefix = bytes(kwargs['prefix'], 'utf-8')

    def run(self):
        curr_drop = self.inputs[0]
        output = self.outputs[0]
        all_lines = BytesIO(allDropContents(curr_drop)).readlines()
        for line in all_lines:
            output.write(self.prefix + line)


# Initialize our drops
a = InMemoryDROP('a', 'a')
b = PrependResult('b', 'b', prefix='Hello ')
c = FileDROP('c', 'c', filepath=output_fname)

# Link Drops together
a.addConsumer(b)
b.addOutput(c)

# Execute and wait (HACK)
a.write(b"world")
a.setCompleted()
time.sleep(7)

# Inspect Results
for drop in (a, b, c):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(allDropContents(c))
