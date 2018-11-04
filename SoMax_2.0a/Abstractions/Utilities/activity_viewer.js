var GRAPH_FRAME = [-0.9, 0.9, -0.6, 0.9];
var ASPECT = calcAspect();
var memory = new Dict("infos");
var frame = new Frame(GRAPH_FRAME);
var streamviews = [];
var colors = [];
var colors_catalogue = [[0., 0., 0.],  [0.1, 0.5, 0.2], [0.5, 0.3, 0]];
var memory_length = 10.0;


mgraphics.init();
mgraphics.relative_coords = 1;
mgraphics.autofill = 0;

function paint()
{
	ASPECT = calcAspect();
	if (streamviews!=[]) {
	frame.draw_state();
	frame.draw_peaks();
	frame.draw_legend();
	frame.draw_frame(GRAPH_FRAME, ASPECT);
	}
}
function set_dict(dict)
{
	memory = new Dict(dict);
}

function set_path(path)
{
	if (path=="Player") {
		streamviews = [];
		streamviews[0] = "_self";
		str_tmp =  memory.get("streamviews").getkeys();
		if (typeof(str_tmp)=="string") {
			streamviews[streamviews.length] = str_tmp;
		} else {
			for (i=0; i<str_tmp.length; i++) {
				streamviews[streamviews.length] = str_tmp[i];
			}
		}
	} else {
		streamviews = [];
		var paths = path.split(":");
		var current_st = memory.get("streamviews");
		for (var i=0; i<paths.length; i++) {
			if (i==0) {
				current_st = current_st.get(paths[0]).get("atoms");
			} else {
				current_st = current_st.get(paths[i]).get("atoms");
			}
		}
		if (current_st!=undefined) {
			streamviews = current_st.getkeys();
			if (typeof(streamviews)=="string") {
				streamviews = [streamviews];
			} 
		} else {
			streamviews = [paths[paths.length-1]];
		}
	}
	colors = [];
	for (i=0; i<streamviews.length; i++)
	{	
		colors.push(colors_catalogue[i%(colors_catalogue.length)]);
	}
}

function Frame(frame_rect) {
	this.frame_rect = frame_rect;
	this.activity_peaks = [];
	this.current_state = [-1, 0, 0];
	this.draw_frame = function(frame_rect, aspect) {
		with (mgraphics) {
			set_source_rgba(.2, .2, .2, 1.);
			set_line_width(.03);
			move_to(frame_rect[0]*aspect, frame_rect[2]);
			line_to(frame_rect[0]*aspect, frame_rect[3]);
			move_to(frame_rect[0]*aspect, frame_rect[2]);
			line_to(frame_rect[1]*aspect, frame_rect[2]);
			stroke( );
			move_to(0,0);
		}
	};
	
	this.draw_peaks = function () {
		this.len = memory_length;
		for (var i = 0; i<this.activity_peaks.length; i++)
		{
			var pos = this.get_activity_pos(this.activity_peaks[i][0], this.activity_peaks[i][1]);
			
			var rel_x = this.frame_rect[0]+(this.activity_peaks[i][0]/this.len)*(this.frame_rect[1]-this.frame_rect[0]);
			var rel_y = this.frame_rect[2]+(this.activity_peaks[i][1])*(this.frame_rect[3]-this.frame_rect[2]);
			rel_x = rel_x*ASPECT;
			var index = streamviews.indexOf(this.activity_peaks[i][0]);
			color = colors[streamviews.indexOf(this.activity_peaks[i][2])];
			if (color!=undefined) {
			with(mgraphics) {
				set_source_rgb(color[0], color[1], color[2]);
				set_line_width(0.01);
				move_to(pos[0], this.frame_rect[2]);
				line_to(pos[0],pos[1]);
				stroke();
			}
			}
			
		}
	};
	
	this.draw_state = function() {
		this.len = memory_length;
		if (this.current_state[0]!=-1)
		{	
			var pos_deb = this.get_activity_pos(this.current_state[1], 0);
			var pos_end = this.get_activity_pos(this.current_state[1]+this.current_state[2], 1.2);
			mgraphics.set_source_rgba(1, 0, 0,0.5);
			mgraphics.rectangle(pos_deb[0],pos_deb[1], Math.max(pos_end[0]-pos_deb[0], 0.03), pos_deb[1]-pos_end[1]);
			mgraphics.fill();
			sz = mgraphics.text_measure(this.current_state[0].toString());
			mgraphics.select_font_face("Verdana");
			mgraphics.move_to(pos_deb[0], pos_deb[1]-0.1);
			mgraphics.show_text(this.current_state[0].toString());
		}
	};
	
	this.draw_legend = function() {
		var pos_deb = [GRAPH_FRAME[0]*ASPECT, (GRAPH_FRAME[1]-0.4)*ASPECT];
		var pos_deb = [this.frame_rect[0]*ASPECT, this.frame_rect[2]-0.15];
		if (colors!=undefined) {
		with (mgraphics) {
			for (i=0; i<colors.length; i++) {
				mgraphics.set_source_rgba(colors[i][0], colors[i][1], colors[i][2], 1.0); 
				mgraphics.rectangle(pos_deb[0],pos_deb[1], 0.13, 0.13);
				fill(colors[i][0], colors[i][1], colors[i][2], 1.0);
				mgraphics.move_to(pos_deb[0] + 0.2, pos_deb[1]-0.1);
				mgraphics.show_text(streamviews[i]);
				stroke();
				pos_deb[0]+=0.7;
			}
		}
		}
	};
	
	this.get_activity_pos = function(mem_x, mem_y) {
		this.len = memory_length;
		var rel_x = this.frame_rect[0]+(mem_x/this.len)*(this.frame_rect[1]-this.frame_rect[0]);
		var rel_y = this.frame_rect[2]+mem_y*(this.frame_rect[3]-this.frame_rect[2]);
		rel_x = rel_x*ASPECT;
		return [rel_x, rel_y];
	}
		/*select_font_face("Trebuchet MS");
		set_font_size(13);
		text_path("Coucou les copains!");*/
	
}


function activity(peaks_str)
{
	var current_peaks = [];
	peak_list = arrayfromargs(arguments);
	if (!peak_list[0]) {
		return ; 
	}
	for (var i = 0; i<peak_list.length-1; i+=3)
	{
		current_peaks.push([peak_list[i], peak_list[i+1], peak_list[i+2]]);
	}
	frame.activity_peaks = current_peaks;
	mgraphics.redraw();
}

function state(state, offset, duration)
{
	var current_state = [state, offset, duration];
	if (state!=frame.current_state[0])
	{
		frame.current_state = [state, offset, duration];
	}
}


function set_memorylength(duration) {
	memory_length = duration;
}



function calcAspect() {
	var width = this.box.rect[2] - this.box.rect[0];
	var height = this.box.rect[3] - this.box.rect[1];
	return width/height;
}

