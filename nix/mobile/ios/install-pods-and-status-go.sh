#!/usr/bin/env bash

RCTSTATUS_DIR="$STATUS_REACT_HOME/modules/react-native-status/ios/RCTStatus"
targetBasename='Statusgo.framework'

# Compare target folder with source to see if copying is required
if [ -d "$RCTSTATUS_DIR/$targetBasename" ] && \
  diff -q --no-dereference --recursive $RCTSTATUS_DIR/$targetBasename/ $RCTSTATUS_FILEPATH/ > /dev/null; then
  echo "$RCTSTATUS_DIR/$targetBasename already in place"
else
  sourceBasename="$(basename $RCTSTATUS_FILEPATH)"
  echo "Copying $sourceBasename from Nix store to $RCTSTATUS_DIR"
  rm -rf "$RCTSTATUS_DIR/$targetBasename/"
  cp -a $RCTSTATUS_FILEPATH $RCTSTATUS_DIR && chmod -R 755 "$RCTSTATUS_DIR/$targetBasename"
  if [ "$sourceBasename" != "$targetBasename" ]; then
    mv "$RCTSTATUS_DIR/$sourceBasename" "$RCTSTATUS_DIR/$targetBasename"
  fi
  if [ "$(uname)" == 'Darwin' ]; then
    # TODO: remove this patch when we upgrade to a RN version that plays well with the modern build system
    git apply --check $STATUS_REACT_HOME/ios/patches/ios-legacy-build-system.patch 2> /dev/null && \
      git apply $STATUS_REACT_HOME/ios/patches/ios-legacy-build-system.patch || \
      echo "Patch already applied"
    # CocoaPods are trash and can't handle other pod instances running at the same time
    $STATUS_REACT_HOME/scripts/wait-for.sh pod 240
    # TODO: install pods in npm-deps.nix and just copy them here
    pushd $STATUS_REACT_HOME/ios && pod install; popd
  fi
fi
