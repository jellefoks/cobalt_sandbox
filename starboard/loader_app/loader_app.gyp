# Copyright 2019 The Cobalt Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This files contains all targets that should be created by gyp_cobalt by
# default.
{
  'targets': [
    {
      'target_name': 'installation_store_proto',
      'type': 'static_library',
      'sources': [
        'installation_store.pb.cc',
        'installation_store_store.pb.h',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/protobuf/protobuf.gyp:protobuf_lite',
      ],
    },
  ],
}