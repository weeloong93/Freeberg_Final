import numpy as np

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.db.models import Q
from .models import Stock
from bokeh.io import vform,gridplot
from bokeh.charts import Bar
from bokeh.plotting import figure, Figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.charts.attributes import color
from bokeh.models import HoverTool, CrosshairTool, CustomJS, Slider, ColumnDataSource, Range1d, LinearAxis, BoxZoomTool, PreviewSaveTool, ResetTool
import ystockquote
from .ystockquote import get_revenue, get_peg, get_annualized_gain
import datetime as dt
from datetime import datetime

# update

def update(stock1):
    stock1.lastprice = ystockquote.get_price(stock1)
    stock1.volume = ystockquote.get_volume(stock1)
    stock1.price_change = float(ystockquote.get_change(stock1))
    stock1.market_cap = ystockquote.get_market_cap(stock1)
    stock1.get_high = ystockquote.get_52_week_high(stock1)
    stock1.get_low = ystockquote.get_52_week_low(stock1)
    stock1.pb_ratio = ystockquote.get_price_book_ratio(stock1)
    stock1.pe_ratio = ystockquote.get_price_earnings_ratio(stock1)
    stock1.dividend = ystockquote.get_dividend_yield(stock1)
    stock1.peg = get_peg(stock1)
    stock1.revenue = get_revenue(stock1)
    stock1.a_gain = get_annualized_gain(stock1)

    stock1.save()


# Last Weekday
def weekday():
    wtoday = dt.date.today()
    if wtoday.isoweekday == 6:
        day_today = wtoday.day - 1
        working_day = wtoday.replace(day=day_today)
        return working_day

    elif wtoday.isoweekday == 7:
        day_today = wtoday.day - 1
        working_day = wtoday.replace(day=day_today)
        return working_day

    else:
        return wtoday

# Create your views here.

def index(request):
    return render(request, 'stocktracker/index.html')

def allstocks(request):
    stocks = Stock.objects.all()

    query = request.GET.get('q')
    if query:
        stocks = stocks.filter(Q(ticker__icontains=query)|
                               Q(company_name__icontains=query)).distinct()

    context = {'stocks': stocks}

    return render(request, 'stocktracker/allstocks.html', context)

def individual_stock(request, stock_id):

    stock1 = get_object_or_404(Stock, pk=stock_id)

    # Stock Information per Stock
    #update(stock1)

    # Graph

    # Last known weekday
    current_day = weekday().isoformat()

    # Retrieve live data YYYY-MM-DD
    historical_price = ystockquote.get_historical_prices(stock1, '2010-01-24', current_day)
    correct_order = sorted(historical_price)
    stock_prices = []
    dates = []
    for values in correct_order:
        stock_prices.append(historical_price[values]['Adj Close'])
        dates.append(values)

    # Convert to Float
    for p in range(len(stock_prices)):
        stock_prices[p] = float(stock_prices[p])

    # Convert to Datetime Format
    dates_objects = []
    for d in dates:
        dates_objects.append(datetime.strptime(d,'%Y-%m-%d'))

    source = ColumnDataSource(data=dict(x=dates_objects,y=stock_prices, time=dates))

    # Tools
    hover = HoverTool(tooltips=[('Stock Price','@y'),('Date','@time'),], mode='vline')
    crosshair = CrosshairTool(dimensions=['height'])

    TOOLS = [BoxZoomTool(),hover, crosshair, PreviewSaveTool(), ResetTool()]

    plot = figure(x_axis_type="datetime", responsive = True ,plot_height=250, tools = TOOLS)
    plot.line('x','y',source=source)
    plot.border_fill = "whitesmoke"

    plot.grid.grid_line_alpha = 0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price'

    #widget
    first_date = dates[0]
    last_date = dates[-1]

    callback = CustomJS(args=dict(x_range=plot.x_range), code="""
                var start = cb_obj.get("value");
                x_range.set("start", start);
                x_range.set("end", start+2);
                """)

    slider = vform(Slider(start=0, end=100, title="Start Date", callback=callback))

    #widget_script, widget_div = components(slider)
    script, div = components(plot)

    stock1.save()
    context = {'stock':stock1,
               'hprice': stock_prices,
               #'widget_script': widget_script,
               #'widget_div': widget_div,
               'the_script': script,
               'the_div':div,
               'thedate': dates_objects,
               'dates':dates
               }

    return render(request, 'stocktracker/individual.html', context)

def pickstock1(request):
    stocks = Stock.objects.all()

    query = request.GET.get('q')
    if query:
        stocks = stocks.filter(Q(ticker__icontains=query) |
                               Q(company_name__icontains=query)).distinct()

    context = {'stocks': stocks}

    return render(request, 'stocktracker/pickstock1.html', context)

def pickstock2(request, stock_id1):
    stock1 = get_object_or_404(Stock, pk=stock_id1)
    stocks = Stock.objects.all()

    query = request.GET.get('q')
    if query:
        stocks = stocks.filter(Q(ticker__icontains=query) |
                               Q(company_name__icontains=query)).distinct()

    context = {'stocks': stocks,
               'stock1': stock1}

    return render(request, 'stocktracker/pickstock2.html', context)

def comparison(request, stock_id1, stock_id2):
    stock1 = get_object_or_404(Stock, pk=stock_id1)
    stock2 = get_object_or_404(Stock, pk=stock_id2)
    #update(stock1)
    #update(stock2)

    # Graph

    # Last known weekday
    current_day = weekday().isoformat()

    # Retrieve live data YYYY-MM-DD
    historical_price1 = ystockquote.get_historical_prices(stock1, '2013-01-24', current_day)
    correct_order1 = sorted(historical_price1)
    stock_prices1 = []
    dates1 = []
    for values in correct_order1:
        stock_prices1.append(historical_price1[values]['Adj Close'])
        dates1.append(values)

    # Convert to Float
    for p in range(len(stock_prices1)):
        stock_prices1[p] = float(stock_prices1[p])

    # Convert to Datetime Format
    dates_objects1 = []
    for d in dates1:
        dates_objects1.append(datetime.strptime(d, '%Y-%m-%d'))

    # Retrieve live data YYYY-MM-DD
    historical_price2 = ystockquote.get_historical_prices(stock2, '2013-01-24', current_day)
    correct_order2 = sorted(historical_price2)
    stock_prices2 = []
    dates2 = []
    for values in correct_order2:
        stock_prices2.append(historical_price2[values]['Adj Close'])
        dates2.append(values)

    # Convert to Float
    for p in range(len(stock_prices2)):
        stock_prices2[p] = float(stock_prices2[p])

    # Convert to Datetime Format
    dates_objects2 = []
    for d in dates2:
        dates_objects2.append(datetime.strptime(d, '%Y-%m-%d'))

    #Tools
    hover = HoverTool(mode='vline')
    crosshair = CrosshairTool(dimensions=['height'])
    TOOLS = [BoxZoomTool(), crosshair, PreviewSaveTool(), ResetTool()]

    p1 = figure(x_axis_type="datetime", responsive=True, plot_height=250,tools=TOOLS)
    p1.border_fill = "whitesmoke"

    # Multiple Axises
    min1 = min(stock_prices1)
    max1 = max(stock_prices1)
    min2 = min(stock_prices2)
    max2 = max(stock_prices2)

    p1.y_range = Range1d(start= min1- (min1/10),end=max1+ (min1/10))
    p1.extra_y_ranges = {'range2':Range1d(start= min2- (min2/10),end=max2+ (min2/10))}
    p1.add_layout(LinearAxis(y_range_name="range2"), 'right')

    p1.line(np.array(dates_objects1, dtype=np.datetime64), stock_prices1, color='#b41f2e', legend=stock1.ticker)
    p1.line(np.array(dates_objects2, dtype=np.datetime64), stock_prices2, y_range_name='range2', color='#1F78B4', legend=stock2.ticker)

    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    script, div = components(p1)

    # Bar Charts
    mc1 = float((stock1.market_cap[:-1]))
    mc2 = float((stock2.market_cap[:-1]))
    pe1 = float(stock1.pe_ratio)
    pe2 = float(stock2.pe_ratio)
    pb1 =float(stock1.pb_ratio)
    pb2 = float(stock2.pb_ratio)
    vol1 = float(stock1.volume)
    vol2 = float(stock2.volume)
    rev1 = float((stock1.revenue[:-1]))
    rev2 = float((stock2.revenue[:-1]))
    peg1 = float(stock1.peg)
    peg2 = float(stock2.peg)

    mc_dict= {'tickers':[stock1.ticker,stock2.ticker],
              'market cap':[mc1,mc2],
              'PB Ratio':[pb1,pb2],
              'PE Ratio':[pe1,pe2],
              'Volume': [vol1,vol2],
              'Revenue': [rev1,rev2],
              'PE Growth': [peg1,peg2]
              }

    #Hover Tools - Not working
    #hover_mc = HoverTool(tooltips=[('Market Cap', '@height'), ('Ticker', '@cat'), ])

    mc_bar = Bar(mc_dict,width=250, height=250,values='market cap',label='tickers',
                 color=color(columns='market cap',palette=['#b41f2e','#1F78B4']), title="Market Cap", ylabel='Billions')
    vol_bar = Bar(mc_dict, width=250, height=250,values='Volume', label='tickers',
                 color=color(columns='Volume',palette=['#b41f2e','#1F78B4']), title="Volume",ylabel='Volume')
    pb_bar = Bar(mc_dict, width=250, height=250,values='PB Ratio', label='tickers',
                 color=color(columns='PB Ratio',palette=['#b41f2e','#1F78B4']),title="PB Ratio",ylabel='Ratio')
    pe_bar = Bar(mc_dict, width=250, height=250,values='PE Ratio', label='tickers',
                 color=color(columns='PE Ratio',palette=['#b41f2e','#1F78B4']),  title="PE Ratio",ylabel='Ratio')
    peg_bar = Bar(mc_dict, width=250, height=250, values='PE Growth', label='tickers',
                 color=color(columns='PE Growth', palette=['#b41f2e', '#1F78B4']), title="PE Growth", ylabel='Percentage(%)')
    rev_bar = Bar(mc_dict, width=250, height=250, values='Revenue', label='tickers',
                 color=color(columns='Revenue', palette=['#b41f2e', '#1F78B4']), title="Revenue", ylabel='Billions')

    mc_bar.border_fill_color = "whitesmoke"
    vol_bar.border_fill_color = "whitesmoke"
    pb_bar.border_fill_color = "whitesmoke"
    pe_bar.border_fill_color = "whitesmoke"
    peg_bar.border_fill_color = "whitesmoke"
    rev_bar.border_fill_color = "whitesmoke"


    grid = gridplot([[mc_bar,rev_bar, pe_bar],[vol_bar, pb_bar, peg_bar]])


    mscript, mdiv = components(grid)

    context = {'stock1': stock1,
               'stock2': stock2,
               'the_script': script,
               'the_div': div,
               'mc1': mscript,
               'mc2': mdiv,
               }

    return render(request, 'stocktracker/comparison.html', context)