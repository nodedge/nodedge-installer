from fbs_runtime.application_context.PyQt5 import ApplicationContext
from nodedge.mdi_window import MdiWindow
# from nodedge.blocks.block_config import *
# from nodedge.blocks.add_block import AddBlock
# from nodedge.blocks import *

import sys

if __name__ == '__main__':
    # associateOperationCodeWithBlock(OP_NODE_ADD, AddBlock)
    appctxt = ApplicationContext()
    window = MdiWindow()
    window.show()
    sys.exit(appctxt.app.exec_())
