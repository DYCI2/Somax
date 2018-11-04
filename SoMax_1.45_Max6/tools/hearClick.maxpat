{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 5,
			"minor" : 1,
			"revision" : 9
		}
,
		"rect" : [ 63.0, 69.0, 140.0, 77.0 ],
		"bglocked" : 0,
		"defrect" : [ 63.0, 69.0, 140.0, 77.0 ],
		"openrect" : [ 0.0, 0.0, 0.0, 0.0 ],
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 0,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 0,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"boxes" : [ 			{
				"box" : 				{
					"maxclass" : "inlet",
					"numinlets" : 0,
					"patching_rect" : [ 80.0, 22.0, 25.0, 25.0 ],
					"numoutlets" : 1,
					"id" : "obj-3",
					"outlettype" : [ "" ],
					"comment" : ""
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "56",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 349.0, 224.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-38",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "42",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 336.0, 200.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-39",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "37",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 322.0, 176.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-40",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "sel 0 1 2",
					"fontsize" : 12.0,
					"numinlets" : 1,
					"patching_rect" : [ 322.0, 150.0, 59.5, 20.0 ],
					"numoutlets" : 4,
					"id" : "obj-24",
					"fontname" : "Arial",
					"outlettype" : [ "bang", "bang", "bang", "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "0",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 322.0, 90.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-21",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "umenu",
					"hint" : "Change the sound of the click",
					"presentation_rect" : [ 5.889038, 42.575897, 74.0, 18.0 ],
					"fontsize" : 10.0,
					"items" : [ "Side", "Stick", ",", "Closed", "Hi-Hat", ",", "Cow", "Bell" ],
					"numinlets" : 1,
					"types" : [  ],
					"patching_rect" : [ 322.0, 122.0, 100.0, 18.0 ],
					"presentation" : 1,
					"numoutlets" : 3,
					"id" : "obj-13",
					"fontname" : "Arial",
					"outlettype" : [ "int", "", "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "loadbang",
					"fontsize" : 12.0,
					"numinlets" : 1,
					"patching_rect" : [ 124.0, 170.0, 60.0, 20.0 ],
					"numoutlets" : 1,
					"id" : "obj-11",
					"fontname" : "Arial",
					"outlettype" : [ "bang" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "set 0",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 265.0, 148.0, 37.0, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-41",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "set 1",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 195.0, 56.0, 37.0, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-42",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "split 1 127",
					"fontsize" : 12.0,
					"numinlets" : 3,
					"patching_rect" : [ 227.0, 318.0, 65.0, 20.0 ],
					"numoutlets" : 2,
					"id" : "obj-43",
					"fontname" : "Arial",
					"outlettype" : [ "int", "int" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "sel 0 1",
					"fontsize" : 12.0,
					"numinlets" : 1,
					"patching_rect" : [ 198.0, 154.0, 46.0, 20.0 ],
					"numoutlets" : 3,
					"id" : "obj-17",
					"fontname" : "Arial",
					"outlettype" : [ "bang", "bang", "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "0",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 189.0, 203.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-44",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "105",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 230.0, 215.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-45",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "textbutton",
					"mode" : 1,
					"texton" : "click on",
					"presentation_rect" : [ 10.889069, 14.575897, 56.013676, 21.798828 ],
					"fontsize" : 12.0,
					"fontlink" : 1,
					"text" : "click off",
					"borderoncolor" : [ 1.0, 0.34902, 0.34902, 1.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 195.0, 101.0, 56.013676, 21.798828 ],
					"presentation" : 1,
					"numoutlets" : 3,
					"id" : "obj-46",
					"fontname" : "Arial",
					"outlettype" : [ "", "", "int" ],
					"bgoncolor" : [ 0.298039, 0.298039, 0.298039, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "comment",
					"text" : "  volume",
					"presentation_rect" : [ 81.889069, 3.075897, 47.0, 18.0 ],
					"fontsize" : 10.0,
					"numinlets" : 1,
					"patching_rect" : [ 223.0, 260.5, 47.0, 18.0 ],
					"presentation" : 1,
					"numoutlets" : 0,
					"id" : "obj-2",
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "dial",
					"hint" : "volume of the click",
					"presentation_rect" : [ 81.889069, 16.075905, 55.0, 55.0 ],
					"numinlets" : 1,
					"patching_rect" : [ 153.0, 247.5, 55.0, 55.0 ],
					"presentation" : 1,
					"numoutlets" : 1,
					"bgcolor" : [ 1.0, 1.0, 1.0, 1.0 ],
					"id" : "obj-1",
					"outlettype" : [ "float" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "comment",
					"text" : "hear click",
					"fontsize" : 12.0,
					"numinlets" : 1,
					"patching_rect" : [ 110.0, 213.5, 65.0, 20.0 ],
					"numoutlets" : 0,
					"id" : "obj-47",
					"fontname" : "Arial"
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "37",
					"fontsize" : 12.0,
					"numinlets" : 2,
					"patching_rect" : [ 80.0, 297.0, 32.5, 18.0 ],
					"numoutlets" : 1,
					"id" : "obj-48",
					"fontname" : "Arial",
					"outlettype" : [ "" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "makenote 120 100 10",
					"fontsize" : 11.595187,
					"numinlets" : 4,
					"patching_rect" : [ 80.0, 318.5, 123.0, 20.0 ],
					"numoutlets" : 3,
					"id" : "obj-4",
					"fontname" : "Arial",
					"outlettype" : [ "float", "float", "float" ]
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "noteout",
					"fontsize" : 12.0,
					"numinlets" : 3,
					"patching_rect" : [ 80.0, 346.0, 123.0, 20.0 ],
					"numoutlets" : 0,
					"id" : "obj-5",
					"fontname" : "Arial"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"source" : [ "obj-38", 0 ],
					"destination" : [ "obj-48", 1 ],
					"hidden" : 0,
					"midpoints" : [ 358.5, 302.0, 123.0, 302.0, 123.0, 293.0, 103.0, 293.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-24", 2 ],
					"destination" : [ "obj-38", 0 ],
					"hidden" : 0,
					"midpoints" : [ 358.5, 185.0, 378.0, 185.0, 378.0, 221.0, 358.5, 221.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-13", 0 ],
					"destination" : [ "obj-24", 0 ],
					"hidden" : 0,
					"midpoints" : [ 331.5, 140.0, 331.5, 140.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-24", 0 ],
					"destination" : [ "obj-40", 0 ],
					"hidden" : 0,
					"midpoints" : [ 331.5, 170.0, 331.5, 170.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-24", 1 ],
					"destination" : [ "obj-39", 0 ],
					"hidden" : 0,
					"midpoints" : [ 345.0, 170.0, 354.0, 170.0, 354.0, 197.0, 345.5, 197.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-40", 0 ],
					"destination" : [ "obj-48", 1 ],
					"hidden" : 0,
					"midpoints" : [ 331.5, 194.0, 231.0, 194.0, 231.0, 188.0, 186.0, 188.0, 186.0, 200.0, 96.0, 200.0, 96.0, 284.0, 103.0, 284.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-39", 0 ],
					"destination" : [ "obj-48", 1 ],
					"hidden" : 0,
					"midpoints" : [ 345.5, 218.0, 273.0, 218.0, 273.0, 245.0, 210.0, 245.0, 210.0, 242.0, 138.0, 242.0, 138.0, 284.0, 103.0, 284.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-21", 0 ],
					"destination" : [ "obj-13", 0 ],
					"hidden" : 0,
					"midpoints" : [ 331.5, 110.0, 331.5, 110.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-11", 0 ],
					"destination" : [ "obj-44", 0 ],
					"hidden" : 0,
					"midpoints" : [ 133.5, 200.0, 198.5, 200.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-41", 0 ],
					"destination" : [ "obj-46", 0 ],
					"hidden" : 0,
					"midpoints" : [ 274.5, 167.0, 261.0, 167.0, 261.0, 86.0, 204.5, 86.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-43", 1 ],
					"destination" : [ "obj-41", 0 ],
					"hidden" : 0,
					"midpoints" : [ 282.5, 338.0, 303.0, 338.0, 303.0, 143.0, 274.5, 143.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-43", 0 ],
					"destination" : [ "obj-42", 0 ],
					"hidden" : 0,
					"midpoints" : [ 236.5, 350.0, 303.0, 350.0, 303.0, 53.0, 204.5, 53.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-42", 0 ],
					"destination" : [ "obj-46", 0 ],
					"hidden" : 0,
					"midpoints" : [ 204.5, 74.0, 204.5, 74.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-45", 0 ],
					"destination" : [ "obj-1", 0 ],
					"hidden" : 0,
					"midpoints" : [ 239.5, 233.0, 162.5, 233.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-44", 0 ],
					"destination" : [ "obj-1", 0 ],
					"hidden" : 0,
					"midpoints" : [ 198.5, 233.0, 162.5, 233.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-46", 0 ],
					"destination" : [ "obj-17", 0 ],
					"hidden" : 0,
					"midpoints" : [ 204.5, 149.0, 207.5, 149.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-17", 0 ],
					"destination" : [ "obj-44", 0 ],
					"hidden" : 0,
					"midpoints" : [ 207.5, 188.0, 198.5, 188.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-17", 1 ],
					"destination" : [ "obj-45", 0 ],
					"hidden" : 0,
					"midpoints" : [ 221.0, 188.0, 239.5, 188.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-43", 0 ],
					"destination" : [ "obj-45", 1 ],
					"hidden" : 0,
					"midpoints" : [ 236.5, 338.0, 222.0, 338.0, 222.0, 290.0, 282.0, 290.0, 282.0, 212.0, 253.0, 212.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-1", 0 ],
					"destination" : [ "obj-43", 0 ],
					"hidden" : 0,
					"midpoints" : [ 162.5, 302.0, 236.5, 302.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-48", 0 ],
					"destination" : [ "obj-4", 0 ],
					"hidden" : 0,
					"midpoints" : [ 89.5, 317.0, 89.5, 317.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-4", 0 ],
					"destination" : [ "obj-5", 0 ],
					"hidden" : 0,
					"midpoints" : [ 89.5, 338.0, 89.5, 338.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-4", 1 ],
					"destination" : [ "obj-5", 1 ],
					"hidden" : 0,
					"midpoints" : [ 141.5, 338.0, 141.5, 338.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-4", 2 ],
					"destination" : [ "obj-5", 2 ],
					"hidden" : 0,
					"midpoints" : [ 193.5, 338.0, 193.5, 338.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-1", 0 ],
					"destination" : [ "obj-4", 1 ],
					"hidden" : 0,
					"midpoints" : [ 162.5, 302.0, 124.166664, 302.0 ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-3", 0 ],
					"destination" : [ "obj-48", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
 ]
	}

}
