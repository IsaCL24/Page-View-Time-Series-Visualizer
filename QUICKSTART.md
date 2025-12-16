# Quick Start Guide

## Project Setup

All required files are already in place:
- ✓ `time_series_visualizer.py` - Main implementation
- ✓ `main.py` - Test runner
- ✓ `test_module.py` - Unit tests
- ✓ `fcc-forum-pageviews.csv` - Sample data (1238 records after cleaning)

## Running the Project

### Generate all visualizations:
```bash
python main.py
```

### Run all unit tests:
```bash
python -m unittest test_module -v
```

## Output

After running, three PNG files are generated:
- `line_plot.png` - Daily trends visualization
- `bar_plot.png` - Monthly averages by year
- `box_plot.png` - Year and month distributions

## Data Processing

The data goes through the following steps:

1. **Import**: CSV file with date and page view count
2. **Parse**: Date column set as index
3. **Clean**: Top and bottom 2.5% filtered out
   - Original: 1304 records
   - Cleaned: 1238 records (98.5%)

## Visualization Details

### Line Plot
- Shows daily page view trends from 5/2016 to 12/2019
- Red line, 12x6 inch figure
- Clear upward trend visible

### Bar Plot
- Average daily views grouped by month and year
- 4 years × 12 months = 48 bars
- Shows seasonal patterns within each year

### Box Plots
- Year-wise: Trend analysis across 4 years (2016-2019)
- Month-wise: Seasonal patterns across 12 months
- Side-by-side comparison format

## Key Statistics

- Average page views: ~14,445 per day
- Range: 4,795 - 24,462 (after cleaning)
- Date span: May 9, 2016 - December 3, 2019 (~3.5 years)

## Requirements

```
pandas>=1.0.0
matplotlib>=3.0.0
seaborn>=0.9.0
```
