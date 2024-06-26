/// do not modify this file! ///
/*used uplugins start
used uplugins end*/

#ifdef __cplusplus
#include <ValueTypes/value.h>
using namespace FlexitekMath::ValueTypes;
extern "C" {
#else
#define fxValue void
#endif

fxValue* __declspec(dllexport) vecsubsum2(fxValue* vec1, fxValue* length);
fxValue* __declspec(dllexport) vecsubsumDescription0();
fxValue* __declspec(dllexport) vecsubsumName0();
fxValue* __declspec(dllexport) crc161(fxValue* data);
fxValue* __declspec(dllexport) crc16Name0();
fxValue* __declspec(dllexport) crc16Description0();
fxValue* __declspec(dllexport) ystep3(fxValue* g1, fxValue* g2, fxValue* step);
fxValue* __declspec(dllexport) ystepDescription0();
fxValue* __declspec(dllexport) ystepName0();
fxValue* __declspec(dllexport) year0();
fxValue* __declspec(dllexport) yearName0();
fxValue* __declspec(dllexport) yearDescription0();
fxValue* __declspec(dllexport) month0();
fxValue* __declspec(dllexport) monthName0();
fxValue* __declspec(dllexport) monthDescription0();
fxValue* __declspec(dllexport) day0();
fxValue* __declspec(dllexport) dayName0();
fxValue* __declspec(dllexport) dayDescription0();
fxValue* __declspec(dllexport) hour0();
fxValue* __declspec(dllexport) hourName0();
fxValue* __declspec(dllexport) hourDescription0();
fxValue* __declspec(dllexport) minute0();
fxValue* __declspec(dllexport) minuteName0();
fxValue* __declspec(dllexport) minuteDescription0();
fxValue* __declspec(dllexport) second0();
fxValue* __declspec(dllexport) secondName0();
fxValue* __declspec(dllexport) secondDescription0();
fxValue* __declspec(dllexport) timef1(fxValue* de);
fxValue* __declspec(dllexport) timefName0();
fxValue* __declspec(dllexport) timefDescription0();
fxValue* __declspec(dllexport) datef1(fxValue* format);
fxValue* __declspec(dllexport) datefName0();
fxValue* __declspec(dllexport) datefDescription0();
fxValue* __declspec(dllexport) datetimef2(fxValue* format, fxValue* de);
fxValue* __declspec(dllexport) datetimefName0();
fxValue* __declspec(dllexport) datetimefDescription0();
fxValue* __declspec(dllexport) timer_create1(fxValue* msec);
fxValue* __declspec(dllexport) timer_createName0();
fxValue* __declspec(dllexport) timer_createDescription0();
fxValue* __declspec(dllexport) timer_delete1(fxValue* tmr);
fxValue* __declspec(dllexport) timer_deleteName0();
fxValue* __declspec(dllexport) timer_deleteDescription0();
fxValue* __declspec(dllexport) event_create0();
fxValue* __declspec(dllexport) event_createName0();
fxValue* __declspec(dllexport) event_createDescription0();
fxValue* __declspec(dllexport) event_emit1(fxValue* evt);
fxValue* __declspec(dllexport) event_emitName0();
fxValue* __declspec(dllexport) timer_emitDescription0();
fxValue* __declspec(dllexport) event_delete1(fxValue* evt);
fxValue* __declspec(dllexport) event_deleteName0();
fxValue* __declspec(dllexport) event_deleteDescription0();
fxValue* __declspec(dllexport) int2floatIEEE1(fxValue* integer);
fxValue* __declspec(dllexport) int2floatIEEEName0();
fxValue* __declspec(dllexport) int2floatIEEEDescription0();
fxValue* __declspec(dllexport) float2intIEEE1(fxValue* float32);
fxValue* __declspec(dllexport) float2intIEEEName0();
fxValue* __declspec(dllexport) float2intIEEEDescription0();
fxValue* __declspec(dllexport) float2arrayIEEE1(fxValue* float32);
fxValue* __declspec(dllexport) float2arrayIEEEDescription0();
fxValue* __declspec(dllexport) array2floatIEEE1(fxValue* array);
fxValue* __declspec(dllexport) array2floatIEEEDescription0();
fxValue* __declspec(dllexport) to_vector1(fxValue* str);
fxValue* __declspec(dllexport) to_vectorName0();
fxValue* __declspec(dllexport) to_vectorDescription0();
fxValue* __declspec(dllexport) json2mat1(fxValue* str);
fxValue* __declspec(dllexport) json2matName0();
fxValue* __declspec(dllexport) json2matDescription0();
fxValue* __declspec(dllexport) mat2json1(fxValue* matr);
fxValue* __declspec(dllexport) mat2jsonName0();
fxValue* __declspec(dllexport) mat2jsonDescription0();
fxValue* __declspec(dllexport) json_value2(fxValue* mat, fxValue* name);
fxValue* __declspec(dllexport) json_valueName0();
fxValue* __declspec(dllexport) json_valueDescription0();
fxValue* __declspec(dllexport) json_set_value3(fxValue* mat, fxValue* name, fxValue* value);
fxValue* __declspec(dllexport) json_set_valueName0();
fxValue* __declspec(dllexport) json_set_valueDescription0();
fxValue* __declspec(dllexport) static_text_box5(fxValue* parent, fxValue* width, fxValue* height, fxValue* font_name, fxValue* font_size);
fxValue* __declspec(dllexport) static_text_boxName0();
fxValue* __declspec(dllexport) static_text_boxDescription0();
fxValue* __declspec(dllexport) zip2(fxValue* outFile, fxValue* inFiles);
fxValue* __declspec(dllexport) zipName0();
fxValue* __declspec(dllexport) zipDescription0();
fxValue* __declspec(dllexport) unzip2(fxValue* inFile, fxValue* rootDir);
fxValue* __declspec(dllexport) unzipName0();
fxValue* __declspec(dllexport) unzipDescription0();
fxValue* __declspec(dllexport) unzip_clear1(fxValue* rootDir);
fxValue* __declspec(dllexport) unzip_clearName0();
fxValue* __declspec(dllexport) unzip_clearDescription0();
fxValue* __declspec(dllexport) document_cursor_insert_template2(fxValue* group, fxValue* name);
fxValue* __declspec(dllexport) document_cursor_insert_templateName0();
fxValue* __declspec(dllexport) document_cursor_insert_templateDescription0();
fxValue* __declspec(dllexport) document_cursor_insert1(fxValue* text);
fxValue* __declspec(dllexport) document_cursor_insertName0();
fxValue* __declspec(dllexport) document_cursor_insertDescription0();
fxValue* __declspec(dllexport) document_cursor_delete0();
fxValue* __declspec(dllexport) document_cursor_deleteName0();
fxValue* __declspec(dllexport) document_cursor_deleteDescription0();
fxValue* __declspec(dllexport) evaluate_document0();
fxValue* __declspec(dllexport) evaluate_documentName0();
fxValue* __declspec(dllexport) evaluate_documentDescription0();
fxValue* __declspec(dllexport) set_image_widget_color5(fxValue* wgt, fxValue* r, fxValue* b, fxValue* g, fxValue* a);
fxValue* __declspec(dllexport) set_image_widget_colorName5(fxValue* wgt, fxValue* r, fxValue* b, fxValue* g, fxValue* a);
fxValue* __declspec(dllexport) set_image_widget_colorDescription0();
fxValue* __declspec(dllexport) set_widget_font_color6(fxValue* wgt, fxValue* r, fxValue* b, fxValue* g, fxValue* a, fxValue* child);
fxValue* __declspec(dllexport) set_widget_font_colorName0();
fxValue* __declspec(dllexport) set_widget_font_colorDescription0();
fxValue* __declspec(dllexport) set_widget_color6(fxValue* wgt, fxValue* r, fxValue* b, fxValue* g, fxValue* a, fxValue* child);
fxValue* __declspec(dllexport) set_widget_colorName0();
fxValue* __declspec(dllexport) set_widget_colorDescription0();
fxValue* __declspec(dllexport) set_widget_on_top1(fxValue* wgt);
fxValue* __declspec(dllexport) set_widget_on_topName0();
fxValue* __declspec(dllexport) set_widget_on_topDescription0();
fxValue* __declspec(dllexport) set_widget_cursor2(fxValue* wgt, fxValue* type);
fxValue* __declspec(dllexport) set_widget_cursorName0();
fxValue* __declspec(dllexport) set_widget_cursorDescription0();
fxValue* __declspec(dllexport) open_url1(fxValue* url);
fxValue* __declspec(dllexport) open_urlName0();
fxValue* __declspec(dllexport) open_urlDescription0();
fxValue* __declspec(dllexport) shell_execute2(fxValue* file, fxValue* command);
fxValue* __declspec(dllexport) shell_executeName0();
fxValue* __declspec(dllexport) shell_executeDescription0();
fxValue* __declspec(dllexport) set_widget_class2(fxValue* wgt, fxValue* cls);
fxValue* __declspec(dllexport) set_widget_className0();
fxValue* __declspec(dllexport) set_widget_classDescription0();
fxValue* __declspec(dllexport) widget_class1(fxValue* wgt);
fxValue* __declspec(dllexport) widget_className0();
fxValue* __declspec(dllexport) widget_classDescription0();
fxValue* __declspec(dllexport) tcp_listen1(fxValue* port);
fxValue* __declspec(dllexport) tcp_listenName0();
fxValue* __declspec(dllexport) tcp_listenDescription0();
fxValue* __declspec(dllexport) tcp_accept1(fxValue* server);
fxValue* __declspec(dllexport) tcp_acceptName0();
fxValue* __declspec(dllexport) tcp_acceptDescription0();
fxValue* __declspec(dllexport) widget_document1(fxValue* wgt);
fxValue* __declspec(dllexport) widget_documentName0();
fxValue* __declspec(dllexport) widget_documentDescription0();
fxValue* __declspec(dllexport) variable_value2(fxValue* doc, fxValue* name);
fxValue* __declspec(dllexport) variable_valueName0();
fxValue* __declspec(dllexport) variable_valueDescription0();
fxValue* __declspec(dllexport) set_variable_value3(fxValue* doc, fxValue* name, fxValue* val);
fxValue* __declspec(dllexport) set_variable_valueName0();
fxValue* __declspec(dllexport) set_variable_valueDescription0();
fxValue* __declspec(dllexport) channels_info0();
fxValue* __declspec(dllexport) channels_infoName0();
fxValue* __declspec(dllexport) channels_infoDescription0();
fxValue* __declspec(dllexport) channels_info_get3(fxValue* ci, fxValue* addr, fxValue* port);
fxValue* __declspec(dllexport) channels_info_getName0();
fxValue* __declspec(dllexport) channels_info_getDescription0();
fxValue* __declspec(dllexport) channels_info_table1(fxValue* ci);
fxValue* __declspec(dllexport) channels_info_tableName0();
fxValue* __declspec(dllexport) channels_info_tableDescription0();
fxValue* __declspec(dllexport) gvar_def2(fxValue* name, fxValue* value);
fxValue* __declspec(dllexport) gvar_defName0();
fxValue* __declspec(dllexport) gvar_defDescription0();
fxValue* __declspec(dllexport) gvar_set2(fxValue* name, fxValue* value);
fxValue* __declspec(dllexport) gvar_setName0();
fxValue* __declspec(dllexport) gvar_setDescription0();
fxValue* __declspec(dllexport) gvar_get1(fxValue* name);
fxValue* __declspec(dllexport) gvar_getName0();
fxValue* __declspec(dllexport) gvar_getDescription0();
fxValue* __declspec(dllexport) gvar_undef1(fxValue* name);
fxValue* __declspec(dllexport) gvar_undefName0();
fxValue* __declspec(dllexport) gvar_undefDescription0();
fxValue* __declspec(dllexport) gvar_names0();
fxValue* __declspec(dllexport) gvar_namesName0();
fxValue* __declspec(dllexport) gvar_namesDescription0();
fxValue* __declspec(dllexport) channel_get_desc1(fxValue* channel);
fxValue* __declspec(dllexport) channel_get_descName0();
fxValue* __declspec(dllexport) channel_get_descDescription0();
fxValue* __declspec(dllexport) channel_set_desc2(fxValue* channel, fxValue* vec);
fxValue* __declspec(dllexport) channel_set_descName0();
fxValue* __declspec(dllexport) channel_set_descDescription0();
fxValue* __declspec(dllexport) set_instrument_widget_unit2(fxValue* instrument, fxValue* unit);
fxValue* __declspec(dllexport) set_instrument_widget_unitName0();
fxValue* __declspec(dllexport) set_instrument_widget_unitDescription0();
fxValue* __declspec(dllexport) application_widget3(fxValue* parent, fxValue* application, fxValue* command);
fxValue* __declspec(dllexport) application_widgetName0();
fxValue* __declspec(dllexport) application_widgetDescription0();
fxValue* __declspec(dllexport) bit_set3(fxValue* integ, fxValue* index, fxValue* value);
fxValue* __declspec(dllexport) bit_setDescription0();
fxValue* __declspec(dllexport) bit_get2(fxValue* integ, fxValue* index);
fxValue* __declspec(dllexport) bit_getDescription0();
fxValue* __declspec(dllexport) map3(fxValue* Key, fxValue* Keys, fxValue* Values);
fxValue* __declspec(dllexport) mapDescription0();
fxValue* __declspec(dllexport) is_byte1(fxValue* value);
fxValue* __declspec(dllexport) is_byteDescription0();

#ifdef __cplusplus
}
#endif