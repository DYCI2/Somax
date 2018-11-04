

inlets = 1;
outlets = 1;
var tree = {};
var current_subatoms = [];
var current_subweights = [];
var current_path = "";

function set_dict(n, umenu_name)
{
	player_dict = new Dict(n);
	make_menu(player_dict, umenu_name);
}



function walk_player_tree(dic, depth, result, tree)
{
	var keys = dic.getkeys();
	if (typeof(keys)!= "object") {
		keys = [keys];
	}
	for (var i=0; i<keys.length; i++)
	{
		if (dic.get(keys[i]).get('type')=='Streamview')
		{	
			if (dic.get(keys[i]).getkeys().indexOf("atoms") != -1) {
				result.push(depth+keys[i]);
				walk_player_tree(dic.get(keys[i]).get("atoms"), depth+keys[i]+":", result, tree);
			} else {
				result.push(depth+keys[i]);
			}
			tree[depth+keys[i]] = "streamview";
		} else if (dic.get(keys[i]).get('type')=='Atom') {
			result.push(depth+keys[i])
			tree[depth+keys[i]] = "atom";
		}			
	}
}

var i_1 = 0;
function make_menu(player_dict, umenu_name)
{
		var menu = this.patcher.getnamed(umenu_name);
		menu.clear();
		menu.append("Player");
		tree = {};
		tree["Player"] = "player";
		var i;
		i_1 = i;
		var streamviews = player_dict.get('streamviews');
		var current_path_still_available = undefined;
		if (streamviews!=undefined) {
			var result = [];
			var wlk = walk_player_tree(streamviews, "", result, tree);
			for (i=0; i<result.length; i++)
			{
				menu.append(result[i]);
				if(result[i]==current_path) {
					current_path_still_available = i;
				}
			}
		} else {
			result = ['Player'];
		}
		i_1 = i;
		if (current_path!="") {
			if (current_path_still_available!=undefined) {
				menu.int(current_path_still_available+1);
			} else {
				menu.int(0);
			}
		}
}

function change_to(objective)
{
	var views = ["atom", "streamview", "player"];
	if (objective!="Player") {
		current_path = objective;
	} else {
		current_path = "Player";
	}
	var object_type = tree[objective];
	if (object_type=="atom") {
		load_atom(objective);
	} else if (object_type=="streamview")  {
		load_streamview(objective);
	} else if (object_type=="player") {
		load_player(objective);
	}
	for (var v=0; v<views.length; v++)
	{
		if (object_type==views[v]) {
			this.patcher.getnamed(views[v]).hidden = false;
			//outlet(0, views[v], "load", objective);
		} else {
			this.patcher.getnamed(views[v]).hidden = true;
		}
	}
}


function print_dic(dic)
{
	var i = 0;
	post(dic.getkeys().length);
	for (i=0;i<dic.getkeys().length;i++) {
		post(i);
		post(dic.getkeys()[i], '\n');
	}
}

function load_atom(objective)
{
	var path_split = objective.split(":");
	if (typeof(path_split)=='string') { path_split = [path_split]; }
	var dic = player_dict;
	for (var i=-1; i<path_split.length-1; i++) {
		if(i==-1) { 
			dic = dic.get('streamviews');
		} else {
			dic = dic.get(path_split[i]).get('atoms');
		}
	}
	dic = dic.get(path_split[path_split.length-1]);
	outlet(0, 'atom', 'current_file', dic.get('current_file'));
	outlet(0, 'atom', 'atom_name', objective);
	outlet(0, 'atom', 'label_type', dic.get("label_type"));
	outlet(0, 'atom', 'contents_type', dic.get("contents_type"));
	outlet(0, 'atom', 'current_file', dic.get("current_file"));
	outlet(0, 'atom', 'memory_type', dic.get("memory"));
	outlet(0, 'atom', 'active_atom', dic.get("active"));
}

function load_streamview(objective)
{
	var path_split = objective.split(":");
	if (typeof(path_split)=='string') { path_split = [path_split]; }
	var dic = player_dict;
	for (var i=-1; i<path_split.length-1; i++) {
		if(i==-1) { 
			dic = dic.get('streamviews');
		} else {
			dic = dic.get(path_split[i]).get('atoms');
		}
	}
	dic = dic.get(path_split[path_split.length-1]);
	current_subatoms = [];
	current_subweights = [];
	if (dic.get('atoms')!=undefined) {
		subatoms = dic.get('atoms').getkeys();
		if (typeof(subatoms)=='string') { subatoms = [subatoms]; }
		for (var i=0; i<subatoms.length; i++) {
			streamview = dic.get('atoms').get(subatoms[i]);
			current_subatoms.push(subatoms[i]);
			current_subweights.push(streamview.get('weight'));
		}
		outlet(0, 'streamview', 'subweights', current_subweights);
		outlet(0, 'streamview', 'subatoms', current_subatoms);
	} else {
		outlet(0, 'streamview', 'subweights', 'hidden',1);
	}
}

function load_player(objective)
{
	dic = player_dict;
	streamviews = player_dict.get('streamviews');
	current_subatoms = [];
	current_subweights = [];
	if (player_dict.get('current_streamview')!=undefined) {
	if (player_dict.get('current_streamview').get("atoms")!=undefined) {
		if (player_dict.get('current_streamview').get("atoms").get("_self")!=undefined) {
		current_subatoms.push("_self");
		current_subweights.push(player_dict.get('current_streamview').get("atoms").get("_self").get("weight"));
	} } }
	
	if (streamviews!=undefined) {
	subatoms = streamviews.getkeys();
	if (typeof(subatoms)=='string') { subatoms = [subatoms]; }
	for (var i=0; i<subatoms.length; i++) {
		streamview = streamviews.get(subatoms[i]);
		current_subatoms.push(subatoms[i]);
		current_subweights.push(streamview.get('weight'));
	}
	outlet(0, 'player', 'self_influence', dic.get('self_influence'));
	outlet(0, 'player', 'label_type', dic.get('label_type'));
	outlet(0, 'player', 'contents_type', dic.get('contents_type'));
	outlet(0, 'player', 'nextstate_mod', dic.get('nextstate_mod'));
	outlet(0, 'player', 'subweights', current_subweights);
	outlet(0, 'player', 'subatoms', current_subatoms);
	outlet(0, 'player', 'phase_selectivity', dic.get('phase_selectivity'));
	outlet(0, 'player', 'triggering_mode', dic.get('triggering_mode'));
	}
}


function set_current_subweight(weight, idx)
{
	if (current_path != "") {
		if (current_path=="Player") {
			outlet(0, "server", "set_weight", current_subatoms[idx], weight);
		} else {
 			outlet(0, "server", "set_weight", current_path+':'+current_subatoms[idx], weight);
		}
	} else {
 		outlet(0, "server", "set_weight", current_subatoms[idx], weight);
	
	}
}
