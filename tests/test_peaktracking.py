import numpy as np

from src.Peak_Tracking import calc_diff, extend_matrix_length


def test_calc_diff():
    """Check that difference is calculated correctly and nan is not included"""
    dummy_tracked_matrix = np.empty((4, 29))
    dummy_tracked_matrix[0:3, :] = np.array(
        [
            [
                164.0,
                237.0,
                362.0,
                436.0,
                585.0,
                658.0,
                716.0,
                927.0,
                np.nan,
                989.0,
                1247.0,
                1282.0,
                1314.0,
                np.nan,
                1552.0,
                np.nan,
                np.nan,
                1682.0,
                1843.0,
                1875.0,
                1901.0,
                2146.0,
                2181.0,
                2216.0,
                2445.0,
                2473.0,
                2513.0,
                2535.0,
                2771.0,
            ],
            [
                165.0,
                237.0,
                361.0,
                435.0,
                589.0,
                664.0,
                np.nan,
                930.0,
                963.0,
                988.0,
                np.nan,
                np.nan,
                1308.0,
                1500.0,
                1533.0,
                1553.0,
                1659.0,
                1685.0,
                1849.0,
                1881.0,
                1911.0,
                np.nan,
                2195.0,
                np.nan,
                2449.0,
                2479.0,
                2515.0,
                2545.0,
                2769.0,
            ],
            [
                165.0,
                np.nan,
                361.0,
                435.0,
                590.0,
                657.0,
                719.0,
                928.0,
                961.0,
                989.0,
                np.nan,
                1284.0,
                1313.0,
                1497.0,
                1527.0,
                1553.0,
                1657.0,
                1687.0,
                1843.0,
                1874.0,
                1904.0,
                np.nan,
                2184.0,
                2222.0,
                2463.0,
                np.nan,
                2511.0,
                np.nan,
                2770.0,
            ],
        ]
    )

    dummy_diff_0 = calc_diff(3, 0, 240, dummy_tracked_matrix)
    dummy_diff_1 = calc_diff(3, 1, 240, dummy_tracked_matrix)
    assert dummy_diff_0 == -75
    assert dummy_diff_1 == -3


def test_extend_matrix_length():
    """Check that the returned matrix has extended its length by 1 and 'nan' is added as the new elements"""
    dummy_tracked_matrix = np.array(
        [
            [
                164.0,
                237.0,
                362.0,
                436.0,
                585.0,
                658.0,
                716.0,
                927.0,
                np.nan,
                989.0,
                1247.0,
                1282.0,
                1314.0,
                np.nan,
                1552.0,
                np.nan,
                np.nan,
                1682.0,
                1843.0,
                1875.0,
                1901.0,
                2146.0,
                2181.0,
                2216.0,
                2445.0,
                2473.0,
                2513.0,
                2535.0,
                2771.0,
            ],
            [
                165.0,
                237.0,
                361.0,
                435.0,
                589.0,
                664.0,
                np.nan,
                930.0,
                963.0,
                988.0,
                np.nan,
                np.nan,
                1308.0,
                1500.0,
                1533.0,
                1553.0,
                1659.0,
                1685.0,
                1849.0,
                1881.0,
                1911.0,
                np.nan,
                2195.0,
                np.nan,
                2449.0,
                2479.0,
                2515.0,
                2545.0,
                2769.0,
            ],
            [
                165.0,
                np.nan,
                361.0,
                435.0,
                590.0,
                657.0,
                719.0,
                928.0,
                961.0,
                989.0,
                np.nan,
                1284.0,
                1313.0,
                1497.0,
                1527.0,
                1553.0,
                1657.0,
                1687.0,
                1843.0,
                1874.0,
                1904.0,
                np.nan,
                2184.0,
                2222.0,
                2463.0,
                np.nan,
                2511.0,
                np.nan,
                2770.0,
            ],
        ]
    )
    old_shape = dummy_tracked_matrix.shape
    new_tracked_matrix = extend_matrix_length(dummy_tracked_matrix, 3)
    new_shape = new_tracked_matrix.shape
    assert new_shape[1] == old_shape[1] + 1
    assert np.isnan(new_tracked_matrix[0][3])