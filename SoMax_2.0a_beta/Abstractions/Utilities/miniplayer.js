inlets = 1;
outlets = 2;

function get_atoms(dicname)
{
	var dictionary = new Dict(dicname);
	var tree = {};
	var results = ["Player"];
	var strs = dictionary.get("streamviews");
	if (strs!=undefined) {
		var wlk = walk_player_tree(dictionary.get("streamviews"), "",results, tree);
	}
	outlet(0, results);
}

function get_weights(dicname, path)
{
	var atoms_values;
	var atoms_list;
	var dictionary = new Dict(dicname);
	if (dictionary.get("current_streamview").get("atoms")!=undefined) {
	if (path=="Player")
	{
		dic = dictionary.get("streamviews")
		strs = dic.getkeys();
		if (typeof(strs)=="string") {
			strs = [strs];
		}
		atoms_list = [];
		atoms_values = [];
		for (var i=0; i<strs.length; i++)
		{
			atoms_list.push(strs[i]);
			atoms_values.push(dic.get(strs[i]).get("weight"));
		}
		atoms_list = ["_self"].concat(atoms_list);
		atoms_values = [dictionary.get("current_streamview").get("weight")].concat(atoms_values);
	} else {
		var path_splitted = path.split(":");
		var path_len = path_splitted.length;
		var dic = dictionary.get("streamviews");
		for (var i=0; i<path_splitted.length-1; i++)
		{
			dic = dic.get(path_splitted[i]).get("atoms");
		}
		dic = dic.get(path_splitted[path_len-1]);
		if (dic.getkeys().indexOf("atoms")!=-1) {
			atoms_list = dic.get("atoms").getkeys();
			if (typeof(atoms_list)=="string")
			{
				atoms_list = [atoms_list];
			}
			atoms_values = [];
			for (i=0; i<atoms_list.length; i++) {
				atoms_values.push(dic.get("atoms").get(atoms_list[i]).get("weight"));
			}
		}
	}
	}
	if (atoms_list!=undefined)
	{
		outlet(1, atoms_values);
		outlet(0, atoms_list);
	} else {
		outlet(1, "none");
		outlet(0, "none");
	}
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
