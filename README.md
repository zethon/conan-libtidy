https://docs.conan.io/en/latest/developing_packages/package_dev_flow.html#conan-install

```
conan source .
conan install . -if=build -s build_type=Debug
conan build . -bf=build
conan package . -sf=source -bf=build -pf=package
conan export-pkg . tidy-html5/5.7.28@owl/stable
conan upload tidy-html5/5.7.28@owl/stable -r owl
```

$ cmake ../source -DDISABLE_DEBUG_LOG=1
