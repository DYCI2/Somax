function isDictionaryKey(dict, str)
{
	var current_dict = new Dict(dict);
	var keys = current_dict.getkeys();
	if (typeof(keys)=="string") {
		keys=[keys];
	}
	var bool = 0;
	for (i=0; i<keys.length; i++)
	{
		if (str==keys[i]) {
			bool = 1;
		}
	}
	outlet(0, bool)
}