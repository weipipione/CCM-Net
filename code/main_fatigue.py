from cross_validation import *
from prepare_data import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ######## Data ########
    parser.add_argument('--dataset', type=str, default='Student_Attention_Detection')
    parser.add_argument('--data-path', type=str, default='E://mywork//CCM-Net//dataset//fatigue//data_2channels//')
    parser.add_argument('--subjects', type=int, default=11)
    parser.add_argument('--num-class', type=int, default=2, choices=[2, 3, 4])

    parser.add_argument('--segment', type=int, default=4, help='segment length in seconds')
    parser.add_argument('--trial-duration', type=int, default=117, help='trial duration in seconds')
    parser.add_argument('--overlap', type=float, default=0.5)
    parser.add_argument('--sampling-rate', type=int, default=256)
    parser.add_argument('--data-format', type=str, default='raw')

    ######## Training Process ########
    parser.add_argument('--random-seed', type=int, default=42)
    parser.add_argument('--max-epoch', type=int, default=1)

    parser.add_argument('--learning-rate', type=float, default=1e-3)
    parser.add_argument('--dropout', type=float, default=0.5)

    parser.add_argument('--save-path', default='./save/')
    parser.add_argument('--load-path', default='./save/max-acc.pth')
    parser.add_argument('--gpu', default="0", type=str,
                        help='indices of GPUs to enable (default: all)')
    parser.add_argument('--save-model', type=bool, default=True)
    parser.add_argument('--l2_alpha', type=float, default=1e-5)
    parser.add_argument('--shared_ratio', default=0.4, type=float)
    parser.add_argument('--model', type=str, default='CCMNet')
    parser.add_argument('--is_MCA', type=int, default=True)
    parser.add_argument('--is_MFM', type=int, default=True)
    # True-单模态 EEG
    parser.add_argument('--is_NotMultiModel', type=int, default=False)
    # parser.add_argument('--input-shape', type=tuple, default=(1, 28, 512))
    parser.add_argument('--input-shape_eeg', type=tuple, default=(1, 2, 64))
    parser.add_argument('--input_shape_all', type=tuple, default=(1, 5, 64))
    '''
    kernel_MTM controls the number of MTM
    kernel_MFM controls the number of MFM
    '''
    parser.add_argument('--kernel_MTM', type=int, default=15)
    parser.add_argument('--kernel_MFM', type=int, default=15)
    parser.add_argument('--batch-size', type=int, default=128)
    parser.add_argument('--reproduce', action='store_true')

    args = parser.parse_args()
    sub_to_run = np.arange(args.subjects)
    pd = PrepareData(args)
    pd.run(sub_to_run, split=True, feature=False, expand=True)
    cv = CrossValidation(args)
    seed_all(args.random_seed)
    cv.n_fold_CV(subject=sub_to_run, fold=10, reproduce=args.reproduce)
