# import pytest

# pytest.main(args=["tests"])

from insider import StockInsider

si = StockInsider("sz002516")

si.plot()

si.plot_boll()
