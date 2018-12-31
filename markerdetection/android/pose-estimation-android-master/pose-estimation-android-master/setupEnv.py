valid = False

while( not valid):
    print('\nWhere is the OpenCV-android-sdk directory located? '
    '(input should look like \"\\path\\to\\OpenCV-android-sdk\")')
    sdkDir = input()
    if('OpenCV-android-sdk' not in sdkDir.split('/')[-1]):
        print('Didn\'t see \"OpenCV-android-sdk\" at the end of the path.')
        print('Make sure your path is formatted like \"\\path\\to\\OpenCV-android-sdk\")')
    else:
        valid = True

print(f'Working in {sdkDir}/sdk...')

makefile = open('./app/src/main/jni/Android.mk', 'r')

print(f'file updated: {makefile.name}')
contents = makefile.read()

contents = contents.replace('{}', f'{sdkDir}/sdk')
writeFile = open('./app/src/main/jni/Android.mk', 'w')
writeFile.write(contents)
