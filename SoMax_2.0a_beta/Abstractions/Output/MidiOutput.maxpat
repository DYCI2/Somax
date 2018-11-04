{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 7,
			"minor" : 3,
			"revision" : 3,
			"architecture" : "x86",
			"modernui" : 1
		}
,
		"rect" : [ 181.0, 79.0, 1263.0, 932.0 ],
		"bgcolor" : [ 1.0, 1.0, 1.0, 0.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "int" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 7,
							"minor" : 3,
							"revision" : 3,
							"architecture" : "x86",
							"modernui" : 1
						}
,
						"rect" : [ 0.0, 0.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-12",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 397.0, 133.0, 22.0 ],
									"style" : "",
									"text" : "prepend midievent 176"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-84",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 430.0, 325.0, 50.0, 22.0 ],
									"style" : "",
									"text" : "2000."
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-82",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 341.0, 296.0, 38.0, 22.0 ],
									"style" : "",
									"text" : "- 200"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-72",
									"linecount" : 2,
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 417.0, 206.5, 230.0, 35.0 ],
									"style" : "",
									"text" : "translate bars.beats.units ms @transport somax-server"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-56",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 306.0, 100.0, 83.0, 22.0 ],
									"style" : "",
									"text" : "sprintf 0.%s.0"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-48",
									"linecount" : 2,
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 306.0, 135.5, 230.0, 35.0 ],
									"style" : "",
									"text" : "translate bars.beats.units ms @transport somax-server"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-46",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 261.0, 324.0, 29.5, 22.0 ],
									"style" : "",
									"text" : "del"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-40",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 198.0, 217.5, 197.0, 22.0 ],
									"style" : "",
									"text" : "metro 2n @transport somax-server"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-28",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 251.0, 369.0, 34.0, 22.0 ],
									"style" : "",
									"text" : "64 0"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-24",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 198.0, 369.0, 47.0, 22.0 ],
									"style" : "",
									"text" : "64 127"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-17",
									"maxclass" : "newobj",
									"numinlets" : 7,
									"numoutlets" : 2,
									"outlettype" : [ "int", "" ],
									"patching_rect" : [ 169.0, 420.0, 82.0, 22.0 ],
									"style" : "",
									"text" : "midiformat"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-13",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 198.0, 40.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-29",
									"index" : 2,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 306.0, 40.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-30",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 50.0, 502.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-31",
									"index" : 2,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 169.0, 502.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-12", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-40", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-13", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-17", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-12", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 1,
									"source" : [ "obj-24", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-17", 2 ],
									"disabled" : 0,
									"hidden" : 0,
									"midpoints" : [ 207.5, 392.0, 199.5, 392.0 ],
									"order" : 0,
									"source" : [ "obj-24", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-12", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 1,
									"source" : [ "obj-28", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-17", 2 ],
									"disabled" : 0,
									"hidden" : 0,
									"midpoints" : [ 260.5, 422.0, 199.5, 422.0 ],
									"order" : 0,
									"source" : [ "obj-28", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-56", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-29", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-24", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 1,
									"source" : [ "obj-40", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-46", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 0,
									"source" : [ "obj-40", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-28", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-46", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-40", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-48", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-48", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 1,
									"source" : [ "obj-56", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-72", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 0,
									"source" : [ "obj-56", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-82", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 1,
									"source" : [ "obj-72", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-84", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"order" : 0,
									"source" : [ "obj-72", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-46", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-82", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 797.0, 442.0, 76.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"style" : "",
						"tags" : ""
					}
,
					"style" : "",
					"text" : "p fake pedal"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 642.0, 684.0, 50.0, 22.0 ],
					"style" : "",
					"text" : "108"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 855.0, 377.5, 72.0, 22.0 ],
					"style" : "",
					"text" : "loadmess 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-57",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 855.0, 409.5, 50.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 260.0, 86.5, 50.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-44",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 797.0, 313.0, 24.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 158.0, 86.5, 24.0, 24.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 823.0, 313.0, 72.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 184.0, 86.5, 72.0, 20.0 ],
					"style" : "",
					"text" : "fake pedal"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-47",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 423.0, 296.0, 50.0, 22.0 ],
					"style" : "",
					"text" : "2000."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 7,
							"minor" : 3,
							"revision" : 3,
							"architecture" : "x86",
							"modernui" : 1
						}
,
						"rect" : [ 0.0, 0.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-30",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 105.0, 160.0, 32.5, 18.0 ],
									"style" : "",
									"text" : "2"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-29",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 160.0, 32.5, 18.0 ],
									"style" : "",
									"text" : "1"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-24",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 50.0, 127.0, 129.0, 20.0 ],
									"style" : "",
									"text" : "route absolute relative"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-13",
									"maxclass" : "newobj",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 100.0, 120.0, 20.0 ],
									"style" : "",
									"text" : "r Somax.timing_type"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-31",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 72.5, 238.0, 25.0, 25.0 ],
									"presentation" : 1,
									"presentation_rect" : [ 65.5, 333.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-24", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-13", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-29", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-24", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-24", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-29", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-31", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-30", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 166.5, 214.0, 82.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"style" : "",
						"tags" : ""
					}
,
					"style" : "",
					"text" : "p timing_type"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 303.833344, 255.0, 54.0, 22.0 ],
					"style" : "",
					"text" : "switch 2"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 10.0,
					"id" : "obj-20",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 613.0, 205.0, 33.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 281.0, 28.5, 33.0, 18.0 ],
					"style" : "",
					"text" : "panic"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.913, 0.913, 0.913, 0.75 ],
					"blinkcolor" : [ 0.52549, 0.062745, 0.003922, 1.0 ],
					"id" : "obj-18",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"outlinecolor" : [ 0.32549, 0.345098, 0.372549, 1.0 ],
					"patching_rect" : [ 593.0, 205.0, 18.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 264.0, 28.5, 18.0, 18.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 593.0, 237.5, 58.0, 22.0 ],
					"style" : "",
					"text" : "midiflush"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 98.0, 114.0, 74.0, 22.0 ],
					"style" : "",
					"text" : "prepend set"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-45",
					"index" : 2,
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 551.5, 364.5, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-42",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 604.5, 602.0, 84.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 3.0, 50.5, 59.0, 20.0 ],
					"style" : "",
					"text" : "VST Out"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-41",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 47.0, 520.0, 84.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 3.0, 28.5, 59.0, 20.0 ],
					"style" : "",
					"text" : "MIDI Out"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 259.5, 408.0, 29.5, 22.0 ],
					"style" : "",
					"text" : "t l l"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-38",
					"index" : 3,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 589.5, 683.0, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-35",
					"index" : 2,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 365.5, 679.0, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-34",
					"index" : 1,
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 290.375, 455.5, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"embed" : 1,
					"enablehscroll" : 0,
					"enablevscroll" : 0,
					"id" : "obj-1",
					"lockeddragscroll" : 0,
					"maxclass" : "bpatcher",
					"name" : "channel_plug.maxpat",
					"numinlets" : 3,
					"numoutlets" : 2,
					"offset" : [ -1.0, 1.0 ],
					"outlettype" : [ "signal", "signal" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 7,
							"minor" : 3,
							"revision" : 3,
							"architecture" : "x86",
							"modernui" : 1
						}
,
						"rect" : [ 1650.0, 703.0, 243.0, 27.0 ],
						"bgcolor" : [ 1.0, 1.0, 1.0, 0.0 ],
						"bglocked" : 0,
						"openinpresentation" : 1,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 0,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-7",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 194.0, 73.0, 37.0, 18.0 ],
									"style" : "",
									"text" : "clear"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-34",
									"maxclass" : "toggle",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 76.0, 112.0, 24.0, 24.0 ],
									"presentation" : 1,
									"presentation_rect" : [ 3.0, 1.0, 24.0, 24.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 13.0,
									"id" : "obj-20",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 76.0, 140.0, 70.0, 19.0 ],
									"style" : "",
									"text" : "bypass $1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-19",
									"maxclass" : "button",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 315.0, 112.0, 24.0, 24.0 ],
									"presentation" : 1,
									"presentation_rect" : [ 220.0, 1.0, 24.0, 24.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"align" : 1,
									"fontface" : 1,
									"id" : "obj-13",
									"items" : [ "no plug-in", ",", "Absynth 4 FX 2x8", ",", "Absynth 4 FX", ",", "Absynth 4 Stereo", ",", "Absynth 4 Surround", ",", "Absynth 4", ",", "Kontakt 5 16out", ",", "Kontakt 5 8out", ",", "Kontakt 5", ",", "Pianoteq 5 STAGE", ",", "Absynth 4 FX", ",", "Absynth 4", ",", "AUAudioFilePlayer", ",", "AUBandpass", ",", "AUDelay", ",", "AUDistortion", ",", "AUDynamicsProcessor", ",", "AUFilter", ",", "AUGraphicEQ", ",", "AUHighShelfFilter", ",", "AUHipass", ",", "AULowpass", ",", "AULowShelfFilter", ",", "AUMatrixMixer", ",", "AUMatrixReverb", ",", "AUMixer", ",", "AUMixer3D", ",", "AUMultibandCompressor", ",", "AUMultiChannelMixer", ",", "AUNBandEQ", ",", "AUNetReceive", ",", "AUNetSend", ",", "AUNewTimePitch", ",", "AUParametricEQ", ",", "AUPeakLimiter", ",", "AUPitch", ",", "AURogerBeep", ",", "AUSampleDelay", ",", "AUSampler", ",", "AUScheduledSoundPlayer", ",", "AUSoundFieldPanner", ",", "AUSphericalHeadPanner", ",", "AUVectorPanner", ",", "DLSMusicDevice", ",", "HRTFPanner", ",", "MIDISynth", ",", "Pianoteq 5 STAGE", ",", "RoundTripAAC" ],
									"maxclass" : "umenu",
									"numinlets" : 1,
									"numoutlets" : 3,
									"outlettype" : [ "int", "", "" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 94.0, 112.0, 219.0, 22.0 ],
									"prefix" : "plug",
									"prefix_mode" : 1,
									"presentation" : 1,
									"presentation_rect" : [ 23.0, 1.0, 197.0, 22.0 ],
									"style" : "",
									"textjustification" : 1
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-16",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 94.0, 73.0, 87.0, 20.0 ],
									"saved_object_attributes" : 									{
										"filename" : "get_plugs.js",
										"parameter_enable" : 0
									}
,
									"style" : "",
									"text" : "js get_plugs.js"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-22",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 315.0, 140.0, 37.0, 18.0 ],
									"style" : "",
									"text" : "open"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-11",
									"index" : 3,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 377.0, 200.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"autosave" : 1,
									"bgmode" : 0,
									"border" : 0,
									"clickthrough" : 0,
									"fontname" : "Arial",
									"fontsize" : 12.0,
									"id" : "obj-5",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 8,
									"offset" : [ 0.0, 0.0 ],
									"outlettype" : [ "signal", "signal", "", "list", "int", "", "", "" ],
									"patching_rect" : [ 194.0, 247.0, 164.0, 20.0 ],
									"save" : [ "#N", "vst~", "loaduniqueid", 0, ";" ],
									"saved_object_attributes" : 									{
										"annotation_name" : "",
										"parameter_enable" : 0
									}
,
									"snapshot" : 									{
										"filetype" : "C74Snapshot",
										"version" : 2,
										"minorversion" : 0,
										"name" : "snapshotlist",
										"origin" : "vst~",
										"type" : "list",
										"subtype" : "Undefined",
										"embed" : 1,
										"snapshot" : 										{
											"pluginname" : "Pianoteq 5 STAGE.vst",
											"plugindisplayname" : "Pianoteq 5 STAGE VST",
											"pluginsavedname" : "Pianoteq 5 STAGE VST",
											"pluginsaveduniqueid" : 0,
											"version" : 1,
											"isbank" : 0,
											"isbase64" : 1,
											"blob" : "7230.CMlaKA....fQPMDZ....A.Ec0zF...P.....fPDMfPTXowVdf.kbgMFcoMVY.................vg.PImUKYA..H.VFQETxuA..n....fLvDCNu.iLuHiMc.....UZg41azUVbfLEUAcTQfTiK33RLuHCLwXSLwHSMW8cuOldGEYU8eLkCg0yAjRFarE1pa...zQFcMImA..PD....DQCHDEVZrkGHPIWXiQWZiUF.....Z....LzavkmbocFZzABJikBHx.SL1.RSuQVXxQGcGB...PEZoMGHvIWYyUFcf7lYlUlbyARXfLFakElafL2a04FYr.RduUGHsEVdfvVZqUFHz8FH0MWYfjFcfX1axARduUmbfPVXowVdf.mbgMFcoMVYt.RPrM2afDFHm81ajAxbzElbzklamABbuklazAhYuIGHvIWYvElbo41Yf3VY2ABbxU1bkQ2bt.....fP....Q....PDMfPTXowVdf.kbgMFcoMVY.....rXA..vQRUUU....F....Dv..2DUxsF..TPc.7u.O.BToUFcfPTYfHUZjQVYxA.jpjBd.pRUF.4JjLXL.tRCnAIIpH3A.RBGx.4MsDXB.dySBZFj7DSfNAHOEYEjqnRA+rSfLA3OrYEjC8hJ2.RfX.3PRQvMqnzJkDXDP9CMHTRIxA3Oa0SIMIEjBsBBlHRf5.nPJEHKPlSHBRAf4nTffXxFz.oOvLHSsHTfh.XKJInPPJSOAdEfxriPPthLBAnOrMXIPJSKBxwK7.BfqjlBxzReu7TQPpySJTiRAVEf5L1FPtiOI.XMhHnI6.DAPxCNAtBf7j1QPFTPTHSNAJBfxXFVPhCTB1DIJI3U.hCXAZBj23iA+7zM.FTQCZAIIfBjvDTfxA3M.4AjqDjJ.BiMm8SW7AIL3HEfqT.GvHUf..IIPEHH.RxXsAIOEEHb.xiYG.4OwHXBAkkA.9ibT.ILBEHX.Fza4ASA9AoPlEXN.JjTt.4PTIELsbGfCklNPRzSA5Afv7TMDkVNPVjQDXRLDJALtfBfl7VfoA4PU8BfEskfBACMgAIQZw.fC0D.P1RPE.iMA1AfvzE.DwVUPVjWR.SGAZAfv.VKEkVKPZzVInxMPAXKzvgQiQiJfQEjGwTCqDSf3A3Qsj.jAARfvAXPa0AjBoRfHAnPakvJYvDjCUEBxXTfw.nLfUxPrEncPtTaAx.fKMlfkA4K8zfRdE3L.pTQa8RZF.IR7P.L4Dna.hTZv.SOAZCjj7RfCAHImbFjCMVfHA3PEIXJPJTUJ.SUxAnPlEHAPNTQpAHLgDHAPtRKRXTQg.3PiEnIFkl.qTzMPhhREfzVBl.fHMVFPZjPc.HJJE3BFgif9.IMMAfNGA.POkiHzDXV.pCaZQCaEADa8HhLX.IJFE3dt.0S.hBaANBj87Ufz.XOakfKlUDj9TzBoTTfgAnOfQBj73RfWAHOUEHYobDRPhyRb.iMC9Af3vVHPdSVApAfvjlL2rkKPVCTKvBUAxBfrf0K0.VCPdiQP.SOA9Df2.FBvnDJPZxSBfSQA9Bf371UPlyKBR.Or.Bf4vQRlTUfm.4OKg.f7j1CPBCTAtBfvTjKPJDXR.SBO.3OowlPusCLJoCjEgVKvHwX.VDaR.iYWAIQVYhJFEHVCA0L.RTSfLzXenhYAV.jBozDqHTfd.nPoAEjCkSf0.3PfYDjD8ze.RTZFsBVNAYQnYvKSE3e.VDaH8hMAlAjxnE.FcVf6.nQrsBjGwDO.JCFAJDjunTfu.3KcQvQi0CjHs0AvXVfeAHRr0.LaIAjK81FyfFT.tDaAdvLaEnTPhTU..CYAF.fHAVYvHDJPNTZQrBSABBfCA1NqXFTPdBND7SQAdCfmzSC+XVf0.4PVAvJqEHH.NzXtA4IKIvO7TAfqTUe+bjGmXlSPZRSB3COANCf9zxNPpBN.HDPtAnIRQgP8ThJaQEjEQ1DsTE.uPQfG.XQoYzKrQQKlE3ePxhZDPjZANDfDkVKrjVfbAoJgcfPmEXL.JDagnxay.4JZIvPVEXL.txaSLjYBpAjFEFAA8EAqfUNG8kF.ZjbyEjY8rRUebDXANEjxbVBJol.AklfO.XPmfjLBUgRiQ3FPBiNAB2L9TBfv.PfvA4MqDHG.dC.uLC.c.IOSE3e.xC.J.4OSEHaCIED.9C.AJzP.3AjHoTfQ.HR.nGjKsifb.3R.L.jOAUfTA3S.H3SPB0XHrBWGnjXBbCYDLEXABEfJAPDPA..SAvX2.f.q.ffUAIImI.LjgvShM.RWQ.UiIwReAvJfUPTbE3B.tB.SPE.DPB.KDE.mrD.w.C.Q7D.A1.I.AvJ.A.L.AvL.AvM.A.O.AvO.AvP.A.R.AfR.AvR.AvS.A.T.APT.AvT.A.U.Av+u..TxMWUoTA..zB...f.....jQC.....H....bjbg4FYfPDM.....L....v........pAA..vID..fsPC.........................v.....A...............C....................L....................v.....A....D....P..........A....P..........v8eh3y.....J.......nFD..fdP...FBA..fHD..PhP...KBA..fID..HoP...kBA..1JjB....gYZR+ffzN8SBLm1O3wOW+j0PT8yLN.1Ocf.f+7nOy9yi9L6OO5yr+........XqP.....L....P........bBE...............................D..................fBL...JP.....L....f........pAA..XKj.....................C....H.......fZP...1BI........3O...f+......f.........HMA......3OC....D........mPA...............C....jF.......QP...HAA..vDD...TP...TAA..fED...WP...fAA..HFD...YP...lAA..fFD..fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTZ.........C...9K...Dv...P.C...AD....P...v.A...9C...3O...v.A...AD...HP.....C...AL...HP...f.A..fBD...LP...f.A....H...3O.....C...9C...Dv...P.C...AD...HP...n.A..fBD...Dv...n.A....H....P...P.C..fBD...JP...P.A...BD....P.....C...9C...HP.....A..fBD...DP...P.C....H...HP...P.C....H...3O...f+B...AL...JP...P.C....L....f.....B..fBD...Dv.....C...9K...Dv...P.C..fBD....v...P.C...AL...HP...f+....AL...HP.........BD...3u.....A..fBD...Dv...f+B....L...LP...n.A...AL...Dv.....C...9C...Dv...P.C...9K...3u...v.A...BD...Dv..............3O...P.C....L...LP...P.C...CD...Dv...P.C...AL....P.....L....f........pAA..XKj........f+....9C........2CA....P..........b.....QkYVX0wFcL.......HKD..fzP..fkCA..HOD..n+P..fEDA..uPD..fDQ..PXDA..5QD..lHQ..fkDI.......v8P7....TD..............b.....QkYVX0wFc..........v.....D........GD...gP...PBA..XKDA.......n.C...9K..............................9C...3OC....H.......fZP...1BI........3O...f+.....v.....B.......nFD..fsPB........9C...3O..........v.....A.......vIT...................3OC....D........mPA...............A...............MyLy81LyL2S...................vu....+....9y.....C.......nFD...mP...1BM........3O...f+....9C..........L....f........pAA..XKj........................f+L....f........pAA..XKj........f+....9C........HBM....vA.......pAA..PJD..fpP...sBA...KD..frP...1Bc...................AD...LP...DAA..fDD...SP.........9y.....C.......nFD...mP...1BM........3O...f+....9C.....C.........P...............P.....C....H.............f+H.............f+.....v.....B.............3OB........9C...3O.....L.....A.........XxjI4i+98yO...f+P...................9C...3O.....L....f..............9i.....................MyLK.M....f........pAA..XKj........f+....9C........f+B...7y.....B........GD...rPB........9C...3O.....D....P.....A....n....vTsEFarABRgwFaK....zVYjkVcsgVXrwVL........fFD...3OlYlY+.....fPfUVO..................fpCA...9C...3OE........9C...3OC....zE......fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTW.......f+....9C...3O...f+....9C...3O...f+....9Sb8n3OEtdj+XOJb9C6Qg4OOJbk+DWOJ9ilYl4OOJbk+rGEN9yiBW4OZlYl+fqGk9SyLy3OJb8n+HEtd9ilYl4OWOJj+b8nP9CtdT5Oov0i+DtdT9SOJb4O6Qgi+7nvU9CRgq4O6Qgq+35Qg9C...3Oov0i+HEtd9C...3OgqGk+v0ih9C6Qg4Ob8nn+7Qgq9Cov04OyLyr+rGEt9iqGE5OHEtl+DWOJ9CWOJ5OCWOh+vdTX9SyLy3OT35g+7QgK9C6Qg4ORgqm+rGEN9iqGE5Oov0i+nYlY9CWOJ5OJb8n+XlYl9Cov04OyLyj+7nv09iT354OZlYl+nYl49CtdT5O...n+zLyr9ilYl6OjBWm+fT3Z9SyLy5O8nvk+jBWO9yv0i5O8nvk+PJbc9ilYl4Ow0ip+fT3Z9iT354ORgqm+fT3Z9ydT35OgqGk+XOJb9Cov04O.....L....v........pAA..vID..fsPC........9C...3O...f+...........C....zE......fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTW..............................................PLZVNuHENR8dQUGzKPYDFOPKDd89E1I0Cr1jTudmi34hcUp1qK3tVu3DxD5b8X.xqEaSXuDIUA8fZhOxifWBqttyqp8Ho301aswqaOZyVR8LzKg1C4Vr5t8hva8Rvef160b2ZuaWQm8b3fC0CuETYuxTiw7j8dw1aTg6JuLxn77P2+A2yVlaytlI1i5BQJ51C2mMaOf3hl8TJsRzqyeWHuMlrs7H0QnxiRznaOxQ9Y8lqF.1y+0zZuTWVm8jXGcwiMNtUOtxEj8pS5c0KXfEJO7cnQ8DwYJziiYMPOavu06XL0wx6UXrWOAfQY81AeByyLZRRuOAiT8lza5z68N4TOrMss8jrsmzaEKUZO83Um8TTK50qOjhWOUV9271Q3WxaIAyXO9oT14X18G2iVYEROUtjy7LvCb1q1ZtVurErj8fxLvySI+NausO5W8XD+N1Cr4CTu.....L........3O...f+....9y.....C.......nFD...mP...1BM........3O...f+....9C.....C....L.......fZP...bBA..XKz........f+....9C...3O.....L....v........pAA..vID..fsPC........9C...3O...f+.........3O...f+X........3OZlYl9zLyL8SyLy7OZlYl9f...............................................L....v........pAA..vID..fsPC........9C...3O...f+.....v.....C.......nFD...mP...1BM........3O...f+....9C.....C....L.......fZP...bBA..XKz........f+....9C...3O.....L....v........pAA..vID..fsPC........9C...3O...f+.....P.....A.......vIz.....A.........P...............fSifcOC....XA.......QP...pAA...GD...dP...5AA...HD..ffP...FBA..jHD...iP...PBA..LID...lP...bBA...JD..fnP...jBA..XJD...pP...pBA...KD..fsPV....fGcj7S5k+3OLDlj+fm7T9SSCR4OMMHk+zzfT9SSCR4OpqXj+zzfT9SSCR4OpqXj+jErN9i5JF4OYAqi+jErN9SVv53OmSHW+bNgb8iejnzOZOTK+Dijx6C.....A.........P.....yLyL+XlYl9S.....A....D....fYlY1OMyLi+D.............7BA....fC........+zLyL2SyLyjO....+P....f.....C....P....P.....B....b....P..........3.....D.........zLyL2C...3O.........7K...mP.....................................................H....................fC....P.........................................................................................f.....................N.....A.........................................................................................A....D........3O...PAC....f.....C....D....PA....D....D....v........v+...f9C...7O..PXCygaABL.....E.............Qv...vBC...KL...rvE.........viBWOO................E...............................A..........A....A....L........7O...P+....+C..PiPb3Vf.C....PA.......DAC........rv...vBC...KbA....Jb8H8X5lDqC...............PA..............................P..........P..........C....7nv0+SOJb0ueT3Z+...zJD..........T........Tv...PAC..vIL...mv...bBW...............................T...............................D..........D.........v.....yLyL+x0iB6iqGE1O................E........EL...Tv...bBC..vIL...mvE...............................E...............................A..........A.........L.....tdT7O8nvU+35Qg+C...............PA.......PAC...EL...mv...bBC..vIbA..............................PA..............................P..........D..........A....L....vLyLyO.....XlYl9C...YP................†¦n étr"
										}
,
										"snapshotlist" : 										{
											"current_snapshot" : 0,
											"entries" : [ 												{
													"filetype" : "C74Snapshot",
													"version" : 2,
													"minorversion" : 0,
													"name" : "MIDISynth.auinfo",
													"origin" : "Pianoteq 5 STAGE.vst",
													"type" : "VST",
													"subtype" : "Instrument",
													"embed" : 0,
													"snapshot" : 													{
														"pluginname" : "Pianoteq 5 STAGE.vst",
														"plugindisplayname" : "Pianoteq 5 STAGE VST",
														"pluginsavedname" : "Pianoteq 5 STAGE VST",
														"pluginsaveduniqueid" : 0,
														"version" : 1,
														"isbank" : 0,
														"isbase64" : 1,
														"blob" : "7230.CMlaKA....fQPMDZ....A.Ec0zF...P.....fPDMfPTXowVdf.kbgMFcoMVY.................vg.PImUKYA..H.VFQETxuA..n....fLvDCNu.iLuHiMc.....UZg41azUVbfLEUAcTQfTiK33RLuHCLwXSLwHSMW8cuOldGEYU8eLkCg0yAjRFarE1pa...zQFcMImA..PD....DQCHDEVZrkGHPIWXiQWZiUF.....Z....LzavkmbocFZzABJikBHx.SL1.RSuQVXxQGcGB...PEZoMGHvIWYyUFcf7lYlUlbyARXfLFakElafL2a04FYr.RduUGHsEVdfvVZqUFHz8FH0MWYfjFcfX1axARduUmbfPVXowVdf.mbgMFcoMVYt.RPrM2afDFHm81ajAxbzElbzklamABbuklazAhYuIGHvIWYvElbo41Yf3VY2ABbxU1bkQ2bt.....fP....Q....PDMfPTXowVdf.kbgMFcoMVY.....rXA..vQRUUU....F....Dv..2DUxsF..TPc.7u.O.BToUFcfPTYfHUZjQVYxA.jpjBd.pRUF.4JjLXL.tRCnAIIpH3A.RBGx.4MsDXB.dySBZFj7DSfNAHOEYEjqnRA+rSfLA3OrYEjC8hJ2.RfX.3PRQvMqnzJkDXDP9CMHTRIxA3Oa0SIMIEjBsBBlHRf5.nPJEHKPlSHBRAf4nTffXxFz.oOvLHSsHTfh.XKJInPPJSOAdEfxriPPthLBAnOrMXIPJSKBxwK7.BfqjlBxzReu7TQPpySJTiRAVEf5L1FPtiOI.XMhHnI6.DAPxCNAtBf7j1QPFTPTHSNAJBfxXFVPhCTB1DIJI3U.hCXAZBj23iA+7zM.FTQCZAIIfBjvDTfxA3M.4AjqDjJ.BiMm8SW7AIL3HEfqT.GvHUf..IIPEHH.RxXsAIOEEHb.xiYG.4OwHXBAkkA.9ibT.ILBEHX.Fza4ASA9AoPlEXN.JjTt.4PTIELsbGfCklNPRzSA5Afv7TMDkVNPVjQDXRLDJALtfBfl7VfoA4PU8BfEskfBACMgAIQZw.fC0D.P1RPE.iMA1AfvzE.DwVUPVjWR.SGAZAfv.VKEkVKPZzVInxMPAXKzvgQiQiJfQEjGwTCqDSf3A3Qsj.jAARfvAXPa0AjBoRfHAnPakvJYvDjCUEBxXTfw.nLfUxPrEncPtTaAx.fKMlfkA4K8zfRdE3L.pTQa8RZF.IR7P.L4Dna.hTZv.SOAZCjj7RfCAHImbFjCMVfHA3PEIXJPJTUJ.SUxAnPlEHAPNTQpAHLgDHAPtRKRXTQg.3PiEnIFkl.qTzMPhhREfzVBl.fHMVFPZjPc.HJJE3BFgif9.IMMAfNGA.POkiHzDXV.pCaZQCaEADa8HhLX.IJFE3dt.0S.hBaANBj87Ufz.XOakfKlUDj9TzBoTTfgAnOfQBj73RfWAHOUEHYobDRPhyRb.iMC9Af3vVHPdSVApAfvjlL2rkKPVCTKvBUAxBfrf0K0.VCPdiQP.SOA9Df2.FBvnDJPZxSBfSQA9Bf371UPlyKBR.Or.Bf4vQRlTUfm.4OKg.f7j1CPBCTAtBfvTjKPJDXR.SBO.3OowlPusCLJoCjEgVKvHwX.VDaR.iYWAIQVYhJFEHVCA0L.RTSfLzXenhYAV.jBozDqHTfd.nPoAEjCkSf0.3PfYDjD8ze.RTZFsBVNAYQnYvKSE3e.VDaH8hMAlAjxnE.FcVf6.nQrsBjGwDO.JCFAJDjunTfu.3KcQvQi0CjHs0AvXVfeAHRr0.LaIAjK81FyfFT.tDaAdvLaEnTPhTU..CYAF.fHAVYvHDJPNTZQrBSABBfCA1NqXFTPdBND7SQAdCfmzSC+XVf0.4PVAvJqEHH.NzXtA4IKIvO7TAfqTUe+bjGmXlSPZRSB3COANCf9zxNPpBN.HDPtAnIRQgP8ThJaQEjEQ1DsTE.uPQfG.XQoYzKrQQKlE3ePxhZDPjZANDfDkVKrjVfbAoJgcfPmEXL.JDagnxay.4JZIvPVEXL.txaSLjYBpAjFEFAA8EAqfUNG8kF.ZjbyEjY8rRUebDXANEjxbVBJol.AklfO.XPmfjLBUgRiQ3FPBiNAB2L9TBfv.PfvA4MqDHG.dC.uLC.c.IOSE3e.xC.J.4OSEHaCIED.9C.AJzP.3AjHoTfQ.HR.nGjKsifb.3R.L.jOAUfTA3S.H3SPB0XHrBWGnjXBbCYDLEXABEfJAPDPA..SAvX2.f.q.ffUAIImI.LjgvShM.RWQ.UiIwReAvJfUPTbE3B.tB.SPE.DPB.KDE.mrD.w.C.Q7D.A1.I.AvJ.A.L.AvL.AvM.A.O.AvO.AvP.A.R.AfR.AvR.AvS.A.T.APT.AvT.A.U.Av+u..TxMWUoTA..zB...f.....jQC.....H....bjbg4FYfPDM.....L....v........pAA..vID..fsPC.........................v.....A...............C....................L....................v.....A....D....P..........A....P..........v8eh3y.....J.......nFD..fdP...FBA..fHD..PhP...KBA..fID..HoP...kBA..1JjB....gYZR+ffzN8SBLm1O3wOW+j0PT8yLN.1Ocf.f+7nOy9yi9L6OO5yr+........XqP.....L....P........bBE...............................D..................fBL...JP.....L....f........pAA..XKj.....................C....H.......fZP...1BI........3O...f+......f.........HMA......3OC....D........mPA...............C....jF.......QP...HAA..vDD...TP...TAA..fED...WP...fAA..HFD...YP...lAA..fFD..fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTZ.........C...9K...Dv...P.C...AD....P...v.A...9C...3O...v.A...AD...HP.....C...AL...HP...f.A..fBD...LP...f.A....H...3O.....C...9C...Dv...P.C...AD...HP...n.A..fBD...Dv...n.A....H....P...P.C..fBD...JP...P.A...BD....P.....C...9C...HP.....A..fBD...DP...P.C....H...HP...P.C....H...3O...f+B...AL...JP...P.C....L....f.....B..fBD...Dv.....C...9K...Dv...P.C..fBD....v...P.C...AL...HP...f+....AL...HP.........BD...3u.....A..fBD...Dv...f+B....L...LP...n.A...AL...Dv.....C...9C...Dv...P.C...9K...3u...v.A...BD...Dv..............3O...P.C....L...LP...P.C...CD...Dv...P.C...AL....P.....L....f........pAA..XKj........f+....9C........2CA....P..........b.....QkYVX0wFcL.......HKD..fzP..fkCA..HOD..n+P..fEDA..uPD..fDQ..PXDA..5QD..lHQ..fkDI.......v8P7....TD..............b.....QkYVX0wFc..........v.....D........GD...gP...PBA..XKDA.......n.C...9K..............................9C...3OC....H.......fZP...1BI........3O...f+.....v.....B.......nFD..fsPB........9C...3O..........v.....A.......vIT...................3OC....D........mPA...............A...............MyLy81LyL2S...................vu....+....9y.....C.......nFD...mP...1BM........3O...f+....9C..........L....f........pAA..XKj........................f+L....f........pAA..XKj........f+....9C........HBM....vA.......pAA..PJD..fpP...sBA...KD..frP...1Bc...................AD...LP...DAA..fDD...SP.........9y.....C.......nFD...mP...1BM........3O...f+....9C.....C.........P...............P.....C....H.............f+H.............f+.....v.....B.............3OB........9C...3O.....L.....A.........XxjI4i+98yO...f+P...................9C...3O.....L....f..............9i.....................MyLK.M....f........pAA..XKj........f+....9C........f+B...7y.....B........GD...rPB........9C...3O.....D....P.....A....n....vTsEFarABRgwFaK....zVYjkVcsgVXrwVL........fFD...3OlYlY+.....fPfUVO..................fpCA...9C...3OE........9C...3OC....zE......fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTW.......f+....9C...3O...f+....9C...3O...f+....9Sb8n3OEtdj+XOJb9C6Qg4OOJbk+DWOJ9ilYl4OOJbk+rGEN9yiBW4OZlYl+fqGk9SyLy3OJb8n+HEtd9ilYl4OWOJj+b8nP9CtdT5Oov0i+DtdT9SOJb4O6Qgi+7nvU9CRgq4O6Qgq+35Qg9C...3Oov0i+HEtd9C...3OgqGk+v0ih9C6Qg4Ob8nn+7Qgq9Cov04OyLyr+rGEt9iqGE5OHEtl+DWOJ9CWOJ5OCWOh+vdTX9SyLy3OT35g+7QgK9C6Qg4ORgqm+rGEN9iqGE5Oov0i+nYlY9CWOJ5OJb8n+XlYl9Cov04OyLyj+7nv09iT354OZlYl+nYl49CtdT5O...n+zLyr9ilYl6OjBWm+fT3Z9SyLy5O8nvk+jBWO9yv0i5O8nvk+PJbc9ilYl4Ow0ip+fT3Z9iT354ORgqm+fT3Z9ydT35OgqGk+XOJb9Cov04O.....L....v........pAA..vID..fsPC........9C...3O...f+...........C....zE......fZP...rAA..3FD...bP...xAA..PGD..fcP...3AA..nGD...eP...9AA...HD..PfP...BBA..LHD...gP...EBA..XHD..vgP...HBA..jHD..fhP...KBA..vHD..PiP...NBA..7HD...jP...QBA..HID..vjP...TBA..TID..fkP...WBA..fID..PlP...ZBA..rID...mP...cBA..3ID..vmP...fBA..BJD..PnP..fgBA..HJD..nnP...iBA..NJD...oP..fjBA..TJD..XoP...lBA..ZJD..voP..fmBA..fJD..HpP...oBA..lJD..fpP..fpBA..rJD..3pP...rBA..xJD..PqP..fsBA..3JD..nqP...uBA..9JD...rP..fvBA..DKD..XrP...xBA..JKD..vrP..fyBA..PKD..HsP...0BA..VKD..fsP..f1BA..bKD..3sP...3BA..hKTW..............................................PLZVNuHENR8dQUGzKPYDFOPKDd89E1I0Cr1jTudmi34hcUp1qK3tVu3DxD5b8X.xqEaSXuDIUA8fZhOxifWBqttyqp8Ho301aswqaOZyVR8LzKg1C4Vr5t8hva8Rvef160b2ZuaWQm8b3fC0CuETYuxTiw7j8dw1aTg6JuLxn77P2+A2yVlaytlI1i5BQJ51C2mMaOf3hl8TJsRzqyeWHuMlrs7H0QnxiRznaOxQ9Y8lqF.1y+0zZuTWVm8jXGcwiMNtUOtxEj8pS5c0KXfEJO7cnQ8DwYJziiYMPOavu06XL0wx6UXrWOAfQY81AeByyLZRRuOAiT8lza5z68N4TOrMss8jrsmzaEKUZO83Um8TTK50qOjhWOUV9271Q3WxaIAyXO9oT14X18G2iVYEROUtjy7LvCb1q1ZtVurErj8fxLvySI+NausO5W8XD+N1Cr4CTu.....L........3O...f+....9y.....C.......nFD...mP...1BM........3O...f+....9C.....C....L.......fZP...bBA..XKz........f+....9C...3O.....L....v........pAA..vID..fsPC........9C...3O...f+.........3O...f+X........3OZlYl9zLyL8SyLy7OZlYl9f...............................................L....v........pAA..vID..fsPC........9C...3O...f+.....v.....C.......nFD...mP...1BM........3O...f+....9C.....C....L.......fZP...bBA..XKz........f+....9C...3O.....L....v........pAA..vID..fsPC........9C...3O...f+.....P.....A.......vIz.....A.........P...............fSifcOC....XA.......QP...pAA...GD...dP...5AA...HD..ffP...FBA..jHD...iP...PBA..LID...lP...bBA...JD..fnP...jBA..XJD...pP...pBA...KD..fsPV....fGcj7S5k+3OLDlj+fm7T9SSCR4OMMHk+zzfT9SSCR4OpqXj+zzfT9SSCR4OpqXj+jErN9i5JF4OYAqi+jErN9SVv53OmSHW+bNgb8iejnzOZOTK+Dijx6C.....A.........P.....yLyL+XlYl9S.....A....D....fYlY1OMyLi+D.............7BA....fC........+zLyL2SyLyjO....+P....f.....C....P....P.....B....b....P..........3.....D.........zLyL2C...3O.........7K...mP.....................................................H....................fC....P.........................................................................................f.....................N.....A.........................................................................................A....D........3O...PAC....f.....C....D....PA....D....D....v........v+...f9C...7O..PXCygaABL.....E.............Qv...vBC...KL...rvE.........viBWOO................E...............................A..........A....A....L........7O...P+....+C..PiPb3Vf.C....PA.......DAC........rv...vBC...KbA....Jb8H8X5lDqC...............PA..............................P..........P..........C....7nv0+SOJb0ueT3Z+...zJD..........T........Tv...PAC..vIL...mv...bBW...............................T...............................D..........D.........v.....yLyL+x0iB6iqGE1O................E........EL...Tv...bBC..vIL...mvE...............................E...............................A..........A.........L.....tdT7O8nvU+35Qg+C...............PA.......PAC...EL...mv...bBC..vIbA..............................PA..............................P..........D..........A....L....vLyLyO.....XlYl9C...YP................†¦n étr"
													}
,
													"fileref" : 													{
														"name" : "MIDISynth.auinfo",
														"filename" : "MIDISynth.auinfo.maxsnap",
														"filepath" : "~/Documents/Max 7/Snapshots",
														"filepos" : -1,
														"snapshotfileid" : "038ada7d20cfeeb60d6e61092c7ecf36"
													}

												}
 ]
										}

									}
,
									"style" : "",
									"text" : "vst~",
									"varname" : "vst~",
									"viewvisibility" : 0
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-4",
									"index" : 2,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 298.833313, 317.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-3",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 194.0, 317.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-2",
									"index" : 2,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 339.0, 200.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-1",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 113.0, 200.0, 25.0, 25.0 ],
									"style" : ""
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-1", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-11", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-13", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-13", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-16", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-22", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-19", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-2", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-20", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-22", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-20", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-34", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-3", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-5", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-4", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"midpoints" : [ 224.214279, 285.0, 308.333313, 285.0 ],
									"source" : [ "obj-5", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-13", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-7", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 365.5, 614.0, 243.0, 27.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 64.0, 50.5, 243.0, 27.0 ],
					"viewvisibility" : 1
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-21",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 239.5, 616.5, 49.0, 22.0 ],
					"style" : "",
					"text" : "midiout"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 234.5, 459.5, 44.0, 22.0 ],
					"style" : "",
					"text" : "gate 2"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 249.0, 102.0, 40.0, 22.0 ],
					"style" : "",
					"text" : "t l l l"
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-11",
					"index" : 1,
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 249.0, 34.0, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-9",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 98.0, 161.5, 150.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 3.0, 4.5, 150.0, 20.0 ],
					"style" : "",
					"text" : "69.00 103.00 2.00"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"items" : [ "Raw", "Output", ",", "MIDI", "Output", ",", "VST" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 123.0, 289.0, 100.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 159.5, 4.5, 100.0, 22.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-3",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 32.0, 442.0, 20.0, 23.0 ],
					"style" : "",
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 13.0,
					"id" : "obj-2",
					"items" : [ "AU DLS Synth 1", ",", "from Max 1", ",", "from Max 2" ],
					"labelclick" : 1,
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 32.0, 542.0, 146.0, 23.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 89.0, 28.5, 146.0, 23.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 32.0, 479.5, 55.0, 23.0 ],
					"style" : "",
					"text" : "midiinfo"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-60",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 338.5, 167.0, 42.0, 22.0 ],
					"style" : "",
					"text" : "* 480."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-27",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 338.5, 222.0, 242.0, 22.0 ],
					"style" : "",
					"text" : "translate ticks ms @transport somax-server"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 2,
					"outlettype" : [ "float", "float" ],
					"patching_rect" : [ 259.5, 299.5, 67.0, 22.0 ],
					"style" : "",
					"text" : "makenote"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-37",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 249.0, 71.0, 89.0, 22.0 ],
					"style" : "",
					"text" : "route midi stop"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-36",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "int", "int", "float", "float" ],
					"patching_rect" : [ 259.5, 131.0, 111.750015, 22.0 ],
					"style" : "",
					"text" : "unpack i i f f"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-25",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 259.5, 533.0, 122.0, 23.0 ],
					"style" : "",
					"text" : "prepend midievent"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-26",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 259.5, 495.0, 70.0, 23.0 ],
					"style" : "",
					"text" : "zl group 3"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 259.5, 342.5, 48.0, 22.0 ],
					"style" : "",
					"text" : "pack i i"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 7,
					"numoutlets" : 2,
					"outlettype" : [ "int", "" ],
					"patching_rect" : [ 259.5, 372.5, 194.0, 22.0 ],
					"style" : "",
					"text" : "midiformat"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"grad1" : [ 0.670588, 0.74902, 0.807843, 1.0 ],
					"grad2" : [ 0.803922, 0.898039, 0.909804, 1.0 ],
					"id" : "obj-7",
					"maxclass" : "panel",
					"mode" : 1,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 775.0, 8.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 1.0, -0.5, 315.0, 85.0 ],
					"proportion" : 0.39,
					"style" : ""
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-10", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-14", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-15", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 2 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 1,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 0,
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-2", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 2 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 269.0, 588.0, 599.0, 588.0 ],
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 269.0, 520.0, 269.0, 520.0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 2 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-27", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-36", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 1,
					"source" : [ "obj-36", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 0,
					"source" : [ "obj-36", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 0,
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 293.5, 105.0, 602.5, 105.0 ],
					"source" : [ "obj-37", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"order" : 1,
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-39", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 2 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 806.5, 588.0, 599.0, 588.0 ],
					"source" : [ "obj-40", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 863.5, 588.0, 249.0, 588.0 ],
					"source" : [ "obj-40", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-44", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 561.0, 446.0, 269.0, 446.0 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-57", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-57", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 602.5, 573.0, 249.0, 573.0 ],
					"order" : 1,
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 602.5, 523.0, 269.0, 523.0 ],
					"order" : 0,
					"source" : [ "obj-8", 0 ]
				}

			}
 ]
	}

}
