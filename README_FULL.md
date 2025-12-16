# Page-View-Time-Series-Visualizer

Time series visualization project using Pandas, Matplotlib, and Seaborn to analyze freeCodeCamp forum page views from 2016-05-09 to 2019-12-03.

## Project Overview

This project visualizes time series data through three different chart types:
1. **Line Chart** - Daily page view trends
2. **Bar Chart** - Average monthly page views by year
3. **Box Plots** - Year-wise and month-wise distributions

## Features

- Data cleaning: Filters out top and bottom 2.5% of outliers
- Line plot showing daily trends
- Bar chart with monthly breakdowns by year
- Box plots for trend and seasonality analysis
- All visualizations saved as PNG files

## Files

- `time_series_visualizer.py` - Main implementation with three visualization functions
- `main.py` - Test runner for the visualizations
- `test_module.py` - Unit tests for validation
- `fcc-forum-pageviews.csv` - Sample data file (1304 records from May 2016 to Dec 2019)

## Installation

Install required dependencies:
```bash
pip install pandas matplotlib seaborn
```

## Usage

### Run the visualizations:
```bash
python main.py
```

### Run the tests:
```bash
python -m unittest test_module -v
```

## Output Files

The script generates three PNG files:
- `line_plot.png` - Daily page view trends (103KB)
- `bar_plot.png` - Average monthly views by year (30KB)
- `box_plot.png` - Year and month box plots (40KB)

## Implementation Details

### Data Import and Cleaning
- Data is imported from `fcc-forum-pageviews.csv`
- Index is set to the date column
- Bottom 2.5% and top 2.5% of page views are filtered out to remove outliers

### Functions

#### `draw_line_plot()`
- Creates a line chart showing daily page view trends
- Title: "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
- X-axis: Date
- Y-axis: Page Views
- Uses red color, 1px line width

#### `draw_bar_plot()`
- Displays average daily page views per month grouped by year
- X-axis: Years
- Y-axis: Average Page Views
- Legend shows month labels (Jan-Dec)
- Each bar group represents one year with 12 sub-bars for months

#### `draw_box_plot()`
- Two adjacent subplots:
  1. Year-wise Box Plot (Trend) - Shows distribution across years
  2. Month-wise Box Plot (Seasonality) - Shows distribution across months
- All visualizations use data copies to preserve original data
- Box plots help identify outliers and distribution patterns

## Test Results

All 9 unit tests pass successfully:
- ✓ Data cleaning tests
- ✓ Line plot validation
- ✓ Bar plot validation
- ✓ Box plot validation
