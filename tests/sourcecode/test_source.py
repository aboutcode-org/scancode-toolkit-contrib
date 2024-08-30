#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/aboutcode-org/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/aboutcode-org/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

import os

from commoncode.testcase import FileBasedTesting
from sourcecode.source import Source


class TestSource(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_source_tags(self):
        self._do_test_source(TEST_DATA)

    def _do_test_source(self, testdata):
        for location, expected in testdata.items():
            test_file = self.get_test_loc(location)
            src = Source(test_file)
            result = src.files, src.global_functions, src.local_functions
            assert expected == result


TEST_DATA = {
    'source/ssdeep/match.c': (['match.c'],
                              ['lsh_list_init',
                               'lsh_list_insert',
                               'match_add',
                               'match_compare',
                               'match_init',
                               'match_load',
                               'match_pretty'],
                              []),

    'source/ssdeep/cycles.c': (['cycles.c'],
                               ['done_processing_dir',
                                'have_processed_dir',
                                'processing_dir'],
                               []),
    'source/ssdeep/dig.c': (['dig.c'],
                            ['clean_name',
                             'clean_name_win32',
                             'file_type',
                             'file_type_helper',
                             'is_special_dir',
                             'is_win32_device_file',
                             'process_dir',
                             'process_normal',
                             'process_win32',
                             'remove_double_dirs',
                             'remove_double_slash',
                             'remove_single_dirs',
                             'should_hash',
                             'should_hash_symlink'],
                            []),
    'source/ssdeep/edit_dist.c': (['edit_dist.c'], ['edit_distn'], []),
    'source/ssdeep/engine.c': (['engine.c'], ['hash_file'], []),
    'source/ssdeep/find-file-size.c': (['find-file-size.c'],
                                       ['find_dev_size',
                                        'find_file_size',
                                        'find_file_size',
                                        'midpoint'],
                                       []),
    'source/ssdeep/fuzzy.c': (['fuzzy.c'],
                              ['eliminate_sequences',
                               'fuzzy_compare',
                               'fuzzy_hash_buf',
                               'fuzzy_hash_file',
                               'has_common_substring',
                               'roll_hash',
                               'roll_reset',
                               'score_strings',
                               'ss_destroy',
                               'ss_engine',
                               'ss_init',
                               'ss_update',
                               'sum_hash'],
                              []),
    'source/ssdeep/fuzzy.h': (['fuzzy.h'],
                              ['fuzzy_compare', 'fuzzy_hash_buf', 'fuzzy_hash_file'],
                              []),
    'source/ssdeep/helpers.c': (['helpers.c'],
                                ['chop_line',
                                 'chop_line_tchar',
                                 'find_comma_separated_string',
                                 'find_comma_separated_string_tchar',
                                 'find_next_comma',
                                 'find_next_comma_tchar',
                                 'mm_magic',
                                 'my_basename',
                                 'my_dirname',
                                 'prepare_filename',
                                 'sanity_check',
                                 'shift_string',
                                 'shift_string_tchar',
                                 'try'],
                                []),
    'source/ssdeep/main.c': (['main.c'],
                             ['generate_filename',
                              'initialize_state',
                              'is_absolute_path',
                              'main',
                              'prepare_windows_command_line',
                              'process_cmd_line',
                              'usage'],
                             []),
    'source/ssdeep/main.h': (['main.h'],
                             ['basename',
                              'chop_line',
                              'chop_line_tchar',
                              'display_filename',
                              'done_processing_dir',
                              'fatal_error',
                              'find_comma_separated_string',
                              'find_comma_separated_string_tchar',
                              'find_file_size',
                              'getopt',
                              'hash_file',
                              'have_processed_dir',
                              'internal_error',
                              'match_add',
                              'match_compare',
                              'match_init',
                              'match_load',
                              'match_pretty',
                              'my_basename',
                              'my_dirname',
                              'prepare_filename',
                              'print_error',
                              'print_error_unicode',
                              'print_status',
                              'process_normal',
                              'process_win32',
                              'processing_dir',
                              'sanity_check',
                              'shift_string',
                              'shift_string_tchar'],
                             []),
    'source/ssdeep/match.c': (['match.c'],
                              ['lsh_list_init',
                               'lsh_list_insert',
                               'match_add',
                               'match_compare',
                               'match_init',
                               'match_load',
                               'match_pretty'],
                              []),
    'source/ssdeep/sample.c': (['sample.c'],
                               ['generate_random', 'main', 'write_data'],
                               []),
    'source/ssdeep/ssdeep.h': (['ssdeep.h'], [], []),
    'source/ssdeep/tchar-local.h': (['tchar-local.h'], [], []),
    'source/ssdeep/ui.c': (['ui.c'],
                           ['display_filename',
                            'fatal_error',
                            'internal_error',
                            'print_error',
                            'print_error_unicode',
                            'print_status'],
                           []),

    'source/magick/orig/Drawable.h': (
        ['Drawable.h'],
        ['Coordinate', 'Coordinate', 'Drawable', 'Drawable', 'Drawable', 'DrawableAffine', 'DrawableAffine', 'DrawableArc', 'DrawableBase', 'DrawableBezier', 'DrawableBezier', 'DrawableCircle', 'DrawableClipPath', 'DrawableClipPath', 'DrawableColor', 'DrawableCompositeImage', 'DrawableCompositeImage', 'DrawableDashArray', 'DrawableDashArray', 'DrawableDashArray', 'DrawableDashOffset', 'DrawableEllipse', 'DrawableFillColor', 'DrawableFillColor', 'DrawableFillOpacity', 'DrawableFillRule', 'DrawableFont', 'DrawableFont', 'DrawableFont', 'DrawableGravity', 'DrawableLine', 'DrawableMatte', 'DrawableMiterLimit', 'DrawablePath', 'DrawablePath', 'DrawablePoint', 'DrawablePointSize', 'DrawablePolygon', 'DrawablePolygon', 'DrawablePolyline', 'DrawablePolyline', 'DrawablePopClipPath', 'DrawablePopGraphicContext', 'DrawablePopPattern', 'DrawablePushClipPath', 'DrawablePushClipPath', 'DrawablePushGraphicContext', 'DrawablePushPattern', 'DrawablePushPattern', 'DrawableRectangle', 'DrawableRotation', 'DrawableRoundRectangle', 'DrawableScaling', 'DrawableSkewX', 'DrawableSkewY', 'DrawableStrokeAntialias', 'DrawableStrokeColor', 'DrawableStrokeColor', 'DrawableStrokeLineCap', 'DrawableStrokeLineJoin', 'DrawableStrokeOpacity', 'DrawableStrokeWidth', 'DrawableText', 'DrawableText', 'DrawableTextAntialias', 'DrawableTextAntialias', 'DrawableTextDecoration', 'DrawableTextDecoration', 'DrawableTextUnderColor', 'DrawableTextUnderColor', 'DrawableTranslation', 'DrawableViewbox', 'PathArcAbs', 'PathArcAbs', 'PathArcAbs', 'PathArcArgs', 'PathArcArgs', 'PathArcArgs', 'PathArcRel', 'PathArcRel', 'PathArcRel', 'PathClosePath', 'PathCurvetoAbs', 'PathCurvetoAbs', 'PathCurvetoAbs', 'PathCurvetoArgs', 'PathCurvetoArgs', 'PathCurvetoArgs', 'PathCurvetoRel', 'PathCurvetoRel', 'PathCurvetoRel', 'PathLinetoAbs', 'PathLinetoAbs', 'PathLinetoAbs', 'PathLinetoHorizontalAbs', 'PathLinetoHorizontalRel', 'PathLinetoRel', 'PathLinetoRel', 'PathLinetoRel', 'PathLinetoVerticalAbs', 'PathLinetoVerticalRel', 'PathMovetoAbs', 'PathMovetoAbs', 'PathMovetoAbs', 'PathMovetoRel', 'PathMovetoRel', 'PathMovetoRel', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoRel', 'PathQuadraticCurvetoRel', 'PathQuadraticCurvetoRel', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoRel', 'PathSmoothCurvetoRel', 'PathSmoothCurvetoRel', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoRel', 'PathSmoothQuadraticCurvetoRel', 'PathSmoothQuadraticCurvetoRel', 'VPath', 'VPath', 'VPath', 'VPathBase', 'angle', 'angle', 'arcEnd', 'arcEnd', 'arcStart', 'arcStart', 'centerX', 'centerX', 'centerY', 'centerY', 'clip_path', 'clip_path', 'color', 'color', 'color', 'composition', 'composition', 'copy', 'copy', 'copy', 'copy', 'copy', 'copy', 'cornerHeight', 'cornerHeight', 'cornerWidth', 'cornerWidth', 'dasharray', 'dasharray', 'dasharray', 'decoration', 'decoration', 'encoding', 'endDegrees', 'endDegrees', 'endX', 'endX', 'endY', 'endY', 'filename', 'filename', 'fillRule', 'fillRule', 'flag', 'flag', 'font', 'font', 'gravity', 'gravity', 'height', 'height', 'hight', 'hight', 'image', 'image', 'largeArcFlag', 'largeArcFlag', 'linecap', 'linecap', 'linejoin', 'linejoin', 'lowerRightX', 'lowerRightX', 'lowerRightY', 'lowerRightY', 'magick', 'magick', 'miterlimit', 'miterlimit', 'offset', 'offset', 'opacity', 'opacity', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator =', 'operator =', 'operator =', 'operator =', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'originX', 'originX', 'originY', 'originY', 'paintMethod', 'paintMethod', 'perimX', 'perimX', 'perimY', 'perimY', 'pointSize', 'pointSize', 'radiusX', 'radiusX', 'radiusY', 'radiusY', 'rx', 'rx', 'ry', 'ry', 'startDegrees', 'startDegrees', 'startX', 'startX', 'startY', 'startY', 'sweepFlag', 'sweepFlag', 'sx', 'sx', 'sy', 'sy', 'text', 'text', 'tx', 'tx', 'ty', 'ty', 'upperLeftX', 'upperLeftX', 'upperLeftY', 'upperLeftY', 'width', 'width', 'x', 'x', 'x', 'x', 'x', 'x', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'x2', 'x2', 'x2', 'xAxisRotation', 'xAxisRotation', 'y', 'y', 'y', 'y', 'y', 'y', 'y1', 'y1', 'y1', 'y1', 'y1', 'y1', 'y2', 'y2', 'y2', 'y2', '~Coordinate', '~Drawable', '~DrawableAffine', '~DrawableArc', '~DrawableBase', '~DrawableBezier', '~DrawableCircle', '~DrawableClipPath', '~DrawableColor', '~DrawableCompositeImage', '~DrawableDashArray', '~DrawableDashOffset', '~DrawableEllipse', '~DrawableFillColor', '~DrawableFillOpacity', '~DrawableFillRule', '~DrawableFont', '~DrawableGravity', '~DrawableLine', '~DrawableMatte', '~DrawableMiterLimit', '~DrawablePath', '~DrawablePoint', '~DrawablePointSize', '~DrawablePolygon', '~DrawablePolyline', '~DrawablePopClipPath', '~DrawablePopGraphicContext', '~DrawablePopPattern', '~DrawablePushClipPath', '~DrawablePushGraphicContext', '~DrawablePushPattern', '~DrawableRectangle', '~DrawableRotation', '~DrawableRoundRectangle', '~DrawableScaling', '~DrawableSkewX', '~DrawableSkewY', '~DrawableStrokeAntialias', '~DrawableStrokeColor', '~DrawableStrokeLineCap', '~DrawableStrokeLineJoin', '~DrawableStrokeOpacity', '~DrawableStrokeWidth', '~DrawableText', '~DrawableTextAntialias', '~DrawableTextDecoration', '~DrawableTextUnderColor', '~DrawableTranslation', '~DrawableViewbox', '~PathArcAbs', '~PathArcArgs', '~PathArcRel', '~PathClosePath', '~PathCurvetoAbs', '~PathCurvetoArgs', '~PathCurvetoRel', '~PathLinetoAbs', '~PathLinetoHorizontalAbs', '~PathLinetoHorizontalRel', '~PathLinetoRel', '~PathLinetoVerticalAbs', '~PathLinetoVerticalRel', '~PathMovetoAbs', '~PathMovetoRel', '~PathQuadraticCurvetoAbs', '~PathQuadraticCurvetoArgs', '~PathQuadraticCurvetoRel', '~PathSmoothCurvetoAbs', '~PathSmoothCurvetoRel', '~PathSmoothQuadraticCurvetoAbs', '~PathSmoothQuadraticCurvetoRel', '~VPath', '~VPathBase'], []),

    'source/magick/moded/Drawable.h': (
        ['Drawable.h'],
        ['Coordinate', 'Coordinate', 'Drawable', 'Drawable', 'Drawable', 'DrawableAffine', 'DrawableAffine', 'DrawableArc', 'DrawableBase', 'DrawableBezier', 'DrawableBezier', 'DrawableCircle', 'DrawableClipPath', 'DrawableClipPath', 'DrawableColor', 'DrawableCompositeImage', 'DrawableCompositeImage', 'DrawableDashArray', 'DrawableDashArray', 'DrawableDashArray', 'DrawableDashOffset', 'DrawableEllipse', 'DrawableFillColor', 'DrawableFillColor', 'DrawableFillOpacity', 'DrawableFillRule', 'DrawableFont', 'DrawableFont', 'DrawableFont', 'DrawableGravity', 'DrawableLine', 'DrawableMatte', 'DrawableMiterLimit', 'DrawablePath', 'DrawablePath', 'DrawablePoint', 'DrawablePointSize', 'DrawablePolygon', 'DrawablePolygon', 'DrawablePolyline', 'DrawablePolyline', 'DrawablePopClipPath', 'DrawablePopGraphicContext', 'DrawablePopPattern', 'DrawablePushClipPath', 'DrawablePushClipPath', 'DrawablePushGraphicContext', 'DrawablePushPattern', 'DrawablePushPattern', 'DrawableRectangle', 'DrawableRotation', 'DrawableRoundRectangle', 'DrawableScaling', 'DrawableSkewX', 'DrawableSkewY', 'DrawableStrokeAntialias', 'DrawableStrokeColor', 'DrawableStrokeColor', 'DrawableStrokeLineCap', 'DrawableStrokeLineJoin', 'DrawableStrokeOpacity', 'DrawableStrokeWidth', 'DrawableText', 'DrawableText', 'DrawableTextAntialias', 'DrawableTextAntialias', 'DrawableTextDecoration', 'DrawableTextDecoration', 'DrawableTextUnderColor', 'DrawableTextUnderColor', 'DrawableTranslation', 'DrawableViewbox', 'PathArcAbs', 'PathArcAbs', 'PathArcAbs', 'PathArcArgs', 'PathArcArgs', 'PathArcArgs', 'PathArcRel', 'PathArcRel', 'PathArcRel', 'PathClosePath', 'PathCurvetoAbs', 'PathCurvetoAbs', 'PathCurvetoAbs', 'PathCurvetoArgs', 'PathCurvetoArgs', 'PathCurvetoArgs', 'PathCurvetoRel', 'PathCurvetoRel', 'PathCurvetoRel', 'PathLinetoAbs', 'PathLinetoAbs', 'PathLinetoAbs', 'PathLinetoHorizontalAbs', 'PathLinetoHorizontalRel', 'PathLinetoRel', 'PathLinetoRel', 'PathLinetoRel', 'PathLinetoVerticalAbs', 'PathLinetoVerticalRel', 'PathMovetoAbs', 'PathMovetoAbs', 'PathMovetoAbs', 'PathMovetoRel', 'PathMovetoRel', 'PathMovetoRel', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoAbs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoArgs', 'PathQuadraticCurvetoRel', 'PathQuadraticCurvetoRel', 'PathQuadraticCurvetoRel', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoAbs', 'PathSmoothCurvetoRel', 'PathSmoothCurvetoRel', 'PathSmoothCurvetoRel', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoAbs', 'PathSmoothQuadraticCurvetoRel', 'PathSmoothQuadraticCurvetoRel', 'PathSmoothQuadraticCurvetoRel', 'VPath', 'VPath', 'VPath', 'VPathBase', 'angle', 'angle', 'arcEnd', 'arcEnd', 'arcStart', 'arcStart', 'centerX', 'centerX', 'centerY', 'centerY', 'clip_path', 'clip_path', 'color', 'color', 'color', 'composition', 'composition', 'copy', 'copy', 'copy', 'copy', 'copy', 'copy', 'cornerHeight', 'cornerHeight', 'cornerWidth', 'cornerWidth', 'dasharray', 'dasharray', 'dasharray', 'decoration', 'decoration', 'encoding', 'endDegrees', 'endDegrees', 'endX', 'endX', 'endY', 'endY', 'filename', 'filename', 'fillRule', 'fillRule', 'flag', 'flag', 'font', 'font', 'gravity', 'gravity', 'height', 'height', 'hight', 'hight', 'image', 'image', 'largeArcFlag', 'largeArcFlag', 'linecap', 'linecap', 'linejoin', 'linejoin', 'lowerRightX', 'lowerRightX', 'lowerRightY', 'lowerRightY', 'magick', 'magick', 'miterlimit', 'miterlimit', 'offset', 'offset', 'opacity', 'opacity', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator !=', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator ()', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator <=', 'operator =', 'operator =', 'operator =', 'operator =', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator ==', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'operator >=', 'originX', 'originX', 'originY', 'originY', 'paintMethod', 'paintMethod', 'perimX', 'perimX', 'perimY', 'perimY', 'pointSize', 'pointSize', 'radiusX', 'radiusX', 'radiusY', 'radiusY', 'rx', 'rx', 'ry', 'ry', 'startDegrees', 'startDegrees', 'startX', 'startX', 'startY', 'startY', 'sweepFlag', 'sweepFlag', 'sx', 'sx', 'sy', 'sy', 'text', 'text', 'tx', 'tx', 'ty', 'ty', 'upperLeftX', 'upperLeftX', 'upperLeftY', 'upperLeftY', 'width', 'width', 'x', 'x', 'x', 'x', 'x', 'x', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'x2', 'x2', 'x2', 'xAxisRotation', 'xAxisRotation', 'y', 'y', 'y', 'y', 'y', 'y', 'y1', 'y1', 'y1', 'y1', 'y1', 'y1', 'y2', 'y2', 'y2', 'y2', '~Coordinate', '~Drawable', '~DrawableAffine', '~DrawableArc', '~DrawableBase', '~DrawableBezier', '~DrawableCircle', '~DrawableClipPath', '~DrawableColor', '~DrawableCompositeImage', '~DrawableDashArray', '~DrawableDashOffset', '~DrawableEllipse', '~DrawableFillColor', '~DrawableFillOpacity', '~DrawableFillRule', '~DrawableFont', '~DrawableGravity', '~DrawableLine', '~DrawableMatte', '~DrawableMiterLimit', '~DrawablePath', '~DrawablePoint', '~DrawablePointSize', '~DrawablePolygon', '~DrawablePolyline', '~DrawablePopClipPath', '~DrawablePopGraphicContext', '~DrawablePopPattern', '~DrawablePushClipPath', '~DrawablePushGraphicContext', '~DrawablePushPattern', '~DrawableRectangle', '~DrawableRotation', '~DrawableRoundRectangle', '~DrawableScaling', '~DrawableSkewX', '~DrawableSkewY', '~DrawableStrokeAntialias', '~DrawableStrokeColor', '~DrawableStrokeLineCap', '~DrawableStrokeLineJoin', '~DrawableStrokeOpacity', '~DrawableStrokeWidth', '~DrawableText', '~DrawableTextAntialias', '~DrawableTextDecoration', '~DrawableTextUnderColor', '~DrawableTranslation', '~DrawableViewbox', '~PathArcAbs', '~PathArcArgs', '~PathArcRel', '~PathClosePath', '~PathCurvetoAbs', '~PathCurvetoArgs', '~PathCurvetoRel', '~PathLinetoAbs', '~PathLinetoHorizontalAbs', '~PathLinetoHorizontalRel', '~PathLinetoRel', '~PathLinetoVerticalAbs', '~PathLinetoVerticalRel', '~PathMovetoAbs', '~PathMovetoRel', '~PathQuadraticCurvetoAbs', '~PathQuadraticCurvetoArgs', '~PathQuadraticCurvetoRel', '~PathSmoothCurvetoAbs', '~PathSmoothCurvetoRel', '~PathSmoothQuadraticCurvetoAbs', '~PathSmoothQuadraticCurvetoRel', '~VPath', '~VPathBase'], []),
}
