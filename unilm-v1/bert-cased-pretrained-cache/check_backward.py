import numpy as np
from reprod_log import ReprodDiffHelper

if __name__ == "__main__":
    diff_helper = ReprodDiffHelper()

    info1 = diff_helper.load_info("./back_torch.npy")
    info2 = diff_helper.load_info("./back_paddle.npy")

    diff_helper.compare_info(info1, info2)

    diff_helper.report(
        diff_method="mean", diff_threshold=1e-6, path="./check_backward.log")