{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 5,
			"minor" : 1,
			"revision" : 9
		}
,
		"rect" : [ 61.0, 69.0, 332.0, 259.0 ],
		"bglocked" : 0,
		"defrect" : [ 61.0, 69.0, 332.0, 259.0 ],
		"openrect" : [ 0.0, 0.0, 0.0, 0.0 ],
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 0,
		"gridsize" : [ 10.0, 10.0 ],
		"gridsnaponopen" : 0,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"boxes" : [ 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "t l l",
					"fontsize" : 12.0,
					"patching_rect" : [ 87.5, 320.0, 32.5, 20.0 ],
					"id" : "obj-663",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "prepend setlist",
					"fontsize" : 12.0,
					"patching_rect" : [ 87.5, 345.0, 89.0, 20.0 ],
					"id" : "obj-739",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "t l l",
					"fontsize" : 12.0,
					"patching_rect" : [ 87.5, 241.0, 32.5, 20.0 ],
					"id" : "obj-737",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "vexpr $f1/$f2 @scalarmode 1",
					"fontsize" : 12.0,
					"patching_rect" : [ 87.5, 295.0, 167.0, 20.0 ],
					"id" : "obj-735",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "zl sum",
					"fontsize" : 12.0,
					"patching_rect" : [ 235.5, 270.0, 50.0, 20.0 ],
					"id" : "obj-732",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "multislider",
					"presentation_rect" : [ 8.0, 4.0, 80.0, 59.0 ],
					"contdata" : 1,
					"setminmax" : [ 0.0, 1.0 ],
					"candycane" : 3,
					"patching_rect" : [ 114.5, 128.0, 136.0, 101.0 ],
					"ghostbar" : 15,
					"presentation" : 1,
					"id" : "obj-727",
					"numinlets" : 1,
					"candicane2" : [ 0.733333, 0.062745, 0.062745, 1.0 ],
					"size" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "outlet",
					"patching_rect" : [ 101.0, 402.0, 25.0, 25.0 ],
					"id" : "obj-2",
					"numinlets" : 1,
					"numoutlets" : 0,
					"comment" : ""
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "inlet",
					"patching_rect" : [ 88.0, 24.0, 25.0, 25.0 ],
					"id" : "obj-1",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"comment" : ""
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"source" : [ "obj-1", 0 ],
					"destination" : [ "obj-737", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-737", 0 ],
					"destination" : [ "obj-735", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-737", 1 ],
					"destination" : [ "obj-732", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-727", 0 ],
					"destination" : [ "obj-737", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-739", 0 ],
					"destination" : [ "obj-727", 0 ],
					"hidden" : 0,
					"midpoints" : [ 97.0, 369.0, 74.0, 369.0, 74.0, 104.0, 124.0, 104.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-732", 0 ],
					"destination" : [ "obj-735", 1 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-735", 0 ],
					"destination" : [ "obj-663", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-663", 0 ],
					"destination" : [ "obj-739", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-663", 1 ],
					"destination" : [ "obj-2", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
 ]
	}

}
