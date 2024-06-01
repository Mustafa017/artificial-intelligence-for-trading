from collections import OrderedDict
import pandas as pd
from tests import project_test, assert_output, generate_random_tickers


@project_test
def test_days_to_weeks(fn):
    tickers = generate_random_tickers(3)
    dates = pd.date_range('10/10/2018', periods=28, freq='D')
    resampled_dates = [
        pd.Timestamp('2018-10-14 00:00:00'),
        pd.Timestamp('2018-10-21 00:00:00'),
        pd.Timestamp('2018-10-28 00:00:00'),
        pd.Timestamp('2018-11-04 00:00:00'),
        pd.Timestamp('2018-11-11 00:00:00')]

    fn_inputs = {
        'open_prices': pd.DataFrame(
            [
                [24, 21, 43],
                [14, 22, 41],
                [29, 23, 44],
                [44, 14, 13],
                [31, 28, 34],
                [36, 49, 27],
                [48, 20, 46],
                [48, 37, 27],
                [16, 42, 22],
                [23, 36, 32],
                [13, 31, 28],
                [23, 33, 18],
                [14, 47, 45],
                [28, 21, 31],
                [31, 36, 40],
                [19, 25, 46],
                [30, 46, 48],
                [19, 34, 35],
                [24, 13, 24],
                [48, 15, 39],
                [16, 34, 14],
                [37, 30, 28],
                [34, 24, 20],
                [17, 15, 38],
                [44, 15, 22],
                [24, 36, 28],
                [12, 41, 49],
                [24, 27, 14]],
            dates, tickers),
        'high_prices': pd.DataFrame(
            [
                [48, 48, 43],
                [42, 49, 47],
                [45, 47, 48],
                [48, 46, 48],
                [49, 49, 46],
                [40, 49, 49],
                [49, 44, 49],
                [49, 46, 48],
                [46, 49, 49],
                [49, 47, 47],
                [45, 49, 46],
                [45, 49, 49],
                [49, 48, 48],
                [48, 49, 49],
                [49, 49, 48],
                [48, 48, 49],
                [48, 47, 48],
                [47, 49, 49],
                [47, 49, 49],
                [48, 49, 48],
                [49, 49, 47],
                [48, 47, 48],
                [47, 48, 47],
                [49, 49, 45],
                [49, 49, 49],
                [47, 46, 48],
                [47, 47, 49],
                [49, 49, 46]],
            dates, tickers),
        'low_prices': pd.DataFrame(
            [
                [12, 12, 13],
                [12, 14, 15],
                [13, 14, 12],
                [14, 14, 13],
                [12, 12, 14],
                [12, 12, 12],
                [12, 12, 12],
                [13, 12, 13],
                [12, 12, 13],
                [14, 12, 14],
                [12, 12, 12],
                [13, 14, 16],
                [14, 13, 13],
                [13, 14, 12],
                [14, 12, 14],
                [15, 12, 13],
                [12, 12, 12],
                [12, 13, 15],
                [14, 12, 12],
                [12, 12, 12],
                [12, 14, 13],
                [12, 12, 13],
                [13, 14, 15],
                [12, 12, 12],
                [12, 14, 12],
                [12, 12, 13],
                [12, 12, 12],
                [16, 12, 14]],
            dates, tickers),
        'close_prices': pd.DataFrame(
            [
                [27, 45, 15],
                [40, 49, 40],
                [25, 26, 36],
                [26, 36, 19],
                [25, 34, 46],
                [22, 39, 45],
                [40, 14, 17],
                [42, 46, 33],
                [35, 41, 49],
                [14, 24, 31],
                [41, 18, 13],
                [36, 27, 18],
                [16, 16, 45],
                [37, 24, 16],
                [43, 40, 28],
                [39, 29, 45],
                [38, 20, 43],
                [44, 13, 34],
                [23, 17, 47],
                [25, 14, 38],
                [48, 44, 23],
                [37, 24, 33],
                [40, 28, 17],
                [31, 12, 44],
                [29, 40, 49],
                [18, 30, 13],
                [27, 16, 47],
                [31, 32, 14]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'open_prices_weekly',
            pd.DataFrame(
                [
                    [24, 21, 43],
                    [36, 49, 27],
                    [14, 47, 45],
                    [48, 15, 39],
                    [12, 41, 49]],
                resampled_dates, tickers)),
        (
            'high_prices_weekly',
            pd.DataFrame(
                [
                    [49, 49, 48],
                    [49, 49, 49],
                    [49, 49, 49],
                    [49, 49, 49],
                    [49, 49, 49]],
                resampled_dates, tickers)),
        (
            'low_prices_weekly',
            pd.DataFrame(
                [
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12],
                    [12, 12, 12]],
                resampled_dates, tickers)),
        (
            'close_prices_weekly',
            pd.DataFrame(
                [
                    [25, 34, 46],
                    [36, 27, 18],
                    [23, 17, 47],
                    [18, 30, 13],
                    [31, 32, 14]],
                resampled_dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)
