var canvas, stage, exportRoot;
function init() {
	// --- write your JS code here ---

	canvas = document.getElementById("canvas");
	exportRoot = new lib.logo_povar2();

	stage = new createjs.Stage(canvas);
	stage.addChild(exportRoot);
	stage.update();

	createjs.Ticker.setFPS(lib.properties.fps);
	createjs.Ticker.addEventListener("tick", stage);
}