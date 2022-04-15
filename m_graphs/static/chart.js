var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1000,
  	height: 500,
	layout: {
		backgroundColor: '#ffffff',
		textColor: 'rgba(29,29,29,0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197,203,206,0)',
		},
		horzLines: {
			color: 'rgba(197,203,206,0)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});

var candleSeries = chart.addCandlestickSeries({
	upColor: '#c18df8',
	downColor: '#7b00ff',
	borderDownColor: 'rgba(255,144,0,0)',
	borderUpColor: 'rgba(255,144,0,0)',
	wickDownColor: 'rgb(123,0,255)',
	wickUpColor: 'rgb(193,141,248)',
});

fetch('http://127.0.0.1:5000/history')
	.then((r) => r.json())
	.then(data => {
	     const cdata = data.map(d => {
	       return {time:d[0],open:parseFloat(d[1]),high:parseFloat(d[2]),low:parseFloat(d[3]),close:parseFloat(d[4])}
	     });
		 console.log(cdata)
	     candleSeries.setData(cdata);
	   })