window.onload = function () {

	var chart1 = new CanvasJS.Chart("chartContainer1", {
		animationEnabled: true,
		title:{
			text: "Blood Pressure (Systolic)"
		},
		axisY: {
			title: "Pressure Noted",
			valueFormatString: "#,,.",
			suffix: "mmHg",
			stripLines: [{
				value: 135,
				label: "Recommended"
			}]
		},
		data: [{
			yValueFormatString: "#,### Units",
			xValueFormatString: "YYYY",
			type: "spline",
			dataPoints: [
				{x:1, y: 144},
				{x: 2, y: 157},
				{x: 3, y: 128},
				{x: 4, y: 135},
				{x: 5, y: 172},
				{x: 6, y: 184},
				{x: 7, y: 191},
							]
		}]
	});
	var chart2 = new CanvasJS.Chart("chartContainer2", {
		animationEnabled: true,
		title:{
			text: "Blood Pressure (Diastolic)"
		},
		axisY: {
			title: "Pressure Noted",
			valueFormatString: "#,,.",
			suffix: "mmHg",
			stripLines: [{
				value: 105,
				label: "Recommended"
			}]
		},
		data: [{
			yValueFormatString: "#,### Units",
			xValueFormatString: "YYYY",
			type: "spline",
			dataPoints: [
				{x:1, y: 109},
				{x: 2, y: 112},
				{x: 3, y: 105},
				{x: 4, y: 97},
				{x: 5, y: 103},
				{x: 6, y: 115},
				{x: 7, y: 120},
			]
		}]
	});
	var chart3 = new CanvasJS.Chart("chartContainer3", {
			animationEnabled: true,
			title:{
				text: "Respiration Rate(Beats/min)"
			},
			axisY: {
				title: "Noted",
				valueFormatString: "#,,.",
				suffix: "bpm",
				stripLines: [{
					value: 23,
					label: "Recommended"
				}]
			},
			data: [{
				yValueFormatString: "#,### Units",
				xValueFormatString: "YYYY",
				type: "spline",
				dataPoints: [
					{x:1, y: 25},
					{x: 2, y: 15},
					{x: 3, y: 35},
					{x: 4, y: 27},
					{x: 5, y: 33},
					{x: 6, y: 45},
					{x: 7, y: 30},
				]
			}]
		});
		var chart4 = new CanvasJS.Chart("chartContainer4", {
				animationEnabled: true,
				title:{
					text: "Pulse Rate"
				},
				axisY: {
					title: "Noted",
					valueFormatString: "#,,.",
					suffix: "bpm",
					stripLines: [{
						value: 100,
						label: "Recommended"
					}]
				},
				data: [{
					yValueFormatString: "#,### Units",
					xValueFormatString: "YYYY",
					type: "spline",
					dataPoints: [
						{x:1, y: 80},
						{x: 2, y: 75},
						{x: 3, y: 90},
						{x: 4, y: 110},
						{x: 5, y: 140},
						{x: 6, y: 127},
						{x: 7, y: 105},
					]
				}]
			});
chart1.render();
chart2.render();
chart3.render();
chart4.render();
}
