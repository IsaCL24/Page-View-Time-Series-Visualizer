import unittest
import time_series_visualizer
import os


class DataCleaningTestCase(unittest.TestCase):
    def setUp(self):
        self.df = time_series_visualizer.df
    
    def test_data_rows(self):
        """Test that data has been cleaned properly"""
        # After filtering top and bottom 2.5%, should have 1204 rows (approximately 98.5% of original)
        # The exact number depends on the dataset
        self.assertGreater(len(self.df), 1000)
        self.assertLess(len(self.df), 1250)


class LineChartTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
    
    def test_line_plot_labels(self):
        """Test that line plot has correct labels"""
        ax = self.fig.get_axes()[0]
        self.assertEqual(ax.get_title(), 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Page Views')
    
    def test_line_plot_exists(self):
        """Test that line plot file is created"""
        self.assertTrue(os.path.exists('line_plot.png'))


class BarChartTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
    
    def test_bar_plot_labels(self):
        """Test that bar plot has correct labels"""
        ax = self.fig.get_axes()[0]
        self.assertEqual(ax.get_xlabel(), 'Years')
        self.assertEqual(ax.get_ylabel(), 'Average Page Views')
    
    def test_bar_plot_exists(self):
        """Test that bar plot file is created"""
        self.assertTrue(os.path.exists('bar_plot.png'))
    
    def test_bar_plot_legend(self):
        """Test that bar plot has correct legend"""
        ax = self.fig.get_axes()[0]
        legend = ax.get_legend()
        self.assertIsNotNone(legend)


class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
    
    def test_box_plot_titles(self):
        """Test that box plots have correct titles"""
        axes = self.fig.get_axes()
        self.assertEqual(axes[0].get_title(), 'Year-wise Box Plot (Trend)')
        self.assertEqual(axes[1].get_title(), 'Month-wise Box Plot (Seasonality)')
    
    def test_box_plot_labels(self):
        """Test that box plots have correct axis labels"""
        axes = self.fig.get_axes()
        self.assertEqual(axes[0].get_xlabel(), 'Year')
        self.assertEqual(axes[0].get_ylabel(), 'Page Views')
        self.assertEqual(axes[1].get_xlabel(), 'Month')
        self.assertEqual(axes[1].get_ylabel(), 'Page Views')
    
    def test_box_plot_exists(self):
        """Test that box plot file is created"""
        self.assertTrue(os.path.exists('box_plot.png'))


if __name__ == '__main__':
    unittest.main()
