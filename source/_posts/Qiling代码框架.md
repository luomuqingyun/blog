---
title: Qiling代码框架
date: 2025-05-19 14:42:00
---

```
├─.github GITHUB仓库信息，不用管
│  │  PULL_REQUEST_TEMPLATE.md
│  │  
│  ├─ISSUE_TEMPLATE
│  │      bug_report.md
│  │      feature_request.md
│  │      
│  └─workflows
│          build-ci.yml
│          dockerimage.yml
│          giteesync.yml
│          pythonpublish.yml
│          
├─docs 说明文档，内部附网页链接，不用管
│      API.md
│      bg_page.png
│      DEMO.md
│      DLLX86.txt
│      DLLX8664.txt
│      GDBSERVER-IDA.png
│      GDBSERVER.md
│      qiling1_logo_big.png
│      qiling1_logo_small.png
│      qiling2_logo_big.png
│      qiling2_logo_small.png
│      README.md
│      SETUP.md
│      USAGE.md
│      
├─examples 
│  │  adcache_x86_windows_debug.py
│  │  cachedlls_x8664_windows.py
│  │  crackme_x86_linux.py
│  │  crackme_x86_windows.py
│  │  crackme_x86_windows_auto.py
│  │  crackme_x86_windows_setcallback.py
│  │  crackme_x86_windows_unpatch.py
│  │  doogie_8086_crack.py
│  │  hello_8086_dos.py
│  │  hello_arm_linux_custom_syscall.py
│  │  hello_arm_linux_debug.py
│  │  hello_arm_qnx.py
│  │  hello_arm_qnx_customapi.py
│  │  hello_arm_set_filter.py
│  │  hello_arm_uboot.py
│  │  hello_linuxx8664_intercept.py
│  │  hello_mips32el_linux_debug.py
│  │  hello_mips32el_linux_function_hook.py
│  │  hello_mips32_linux_customapi.py
│  │  hello_x8664_gdb_macos.py
│  │  hello_x8664_linux_customapi.py
│  │  hello_x8664_linux_disasm.py
│  │  hello_x8664_linux_part_debug.py
│  │  hello_x8664_linux_part_exec.py
│  │  hello_x8664_macos.py
│  │  hello_x8664_windows_customapi.py
│  │  hello_x86_linux_fake_urandom.py
│  │  mem_invalid_access.py
│  │  multithreading_arm64_linux.py
│  │  multithreading_mips32el_linux.py
│  │  multithreading_mips32_linux.py
│  │  multithreading_x86_windows.py
│  │  netgear_6220.py
│  │  netgear_6220.ql
│  │  ntQuerySystemInfo_x86.py
│  │  petya_8086_crack.py
│  │  README.md
│  │  regdemo_x86_windows.py
│  │  sality.py
│  │  setexit_arm64_linux.py
│  │  shellcode_run.py
│  │  simple_efi_x8664.py
│  │  tendaac1518_httpd.py
│  │  uboot_bin.ql
│  │  uefi_sanitized_heap.py
│  │  uselessdisk_x86_windows.py
│  │  wannacry_x86_windows_hookaddress.py
│  │  windows_trace.py
│  │  
│  ├─evm
│  │  │  evm_debugger.py
│  │  │  evm_Hexagon_overflow.py
│  │  │  evm_reentrancy.py
│  │  │  evm_reentrancy_vol.py
│  │  │  evm_simple_sc.py
│  │  │  
│  │  └─fuzzing
│  │      │  .gitignore
│  │      │  fuzz.py
│  │      │  fuzz.sh
│  │      │  README.md
│  │      │  underflow_test.py
│  │      │  
│  │      └─input
│  │              input0.txt
│  │              
│  ├─extensions
│  │  ├─idaplugin
│  │  │      custom_script.py
│  │  │      
│  │  ├─r2
│  │  │      hello_r2.py
│  │  │      
│  │  ├─report
│  │  │      hello_x86_windows_json.py
│  │  │      
│  │  └─trace
│  │          trace.py
│  │          
│  ├─fuzzing
│  │  │  .gitignore
│  │  │  
│  │  ├─dlink_dir815
│  │  │  │  dir815_mips32el_linux.py
│  │  │  │  dir815_mips32el_linux.sh
│  │  │  │  
│  │  │  └─afl_inputs
│  │  │          a
│  │  │          
│  │  ├─linux_x8664
│  │  │  │  fuzz.c
│  │  │  │  fuzz.sh
│  │  │  │  fuzz_x8664_linux.py
│  │  │  │  libfuzzer_x8664_linux.py
│  │  │  │  qilingfzz.png
│  │  │  │  README.md
│  │  │  │  x8664_fuzz
│  │  │  │  
│  │  │  └─afl_inputs
│  │  │          a
│  │  │          
│  │  ├─qnx_arm
│  │  │  │  arm_fuzz
│  │  │  │  fuzz.c
│  │  │  │  fuzz.sh
│  │  │  │  fuzz_arm_qnx.py
│  │  │  │  README.md
│  │  │  │  
│  │  │  └─afl_inputs
│  │  │          a
│  │  │          
│  │  ├─stm32f429
│  │  │  │  fuzz.py
│  │  │  │  fuzz.sh
│  │  │  │  
│  │  │  └─afl_inputs
│  │  │          sample
│  │  │          
│  │  └─tenda_ac15
│  │      │  addressNat_overflow.sh
│  │      │  fuzz_tendaac15_httpd.py
│  │      │  fuzz_tendaac15_httpd.sh
│  │      │  README.md
│  │      │  saver_tendaac15_httpd.py
│  │      │  
│  │      └─afl_inputs
│  │              a
│  │              
│  ├─mcu
│  │      gd32vf103_blink.py
│  │      stm32f407_gpio_hook.py
│  │      stm32f407_hack_lock.py
│  │      stm32f407_mnist_oled.py
│  │      stm32f411_dma_logger.py
│  │      stm32f411_freertos.py
│  │      stm32f411_gpio_hook.py
│  │      stm32f411_i2c_lcd.py
│  │      stm32f411_interact_usart.py
│  │      stm32f411_spi_oled12864.py
│  │      
│  ├─rootfs
│  ├─scripts
│  │      dllscollector.bat
│  │      dylibcollector.sh
│  │      
│  ├─shellcodes
│  │      bsd64_tcp_bind_shell.hex
│  │      lin32_encoded_execve.hex
│  │      lin32_execve.asm
│  │      lin32_ob_execve.hex
│  │      lin64_execve.hex
│  │      lin64_unknown.hex
│  │      linarm32_tcp_reverse_shell.hex
│  │      linarm64_tcp_reverse_shell.hex
│  │      linarm_chmod_shadow.hex
│  │      linarm_mprotect_egghunter
│  │      linarm_quantum_leap_stub
│  │      linmips32_tcp_reverse_shell.hex
│  │      linmips_execve.hex
│  │      linux_x86_shell_reverse_tcp.asm
│  │      linux_x86_shell_reverse_tcp.bin
│  │      macos64_execve.hex
│  │      macos64_tcp_reverse_shell.hex
│  │      win32_https_download.zip
│  │      win32_ob_exec_calc.asm
│  │      win32_ob_exec_calc.bin
│  │      win32_ob_exec_calc.hex
│  │      win32_ob_msg_box.bin
│  │      win32_ob_shell_reverse_tcp.asm
│  │      win32_ob_shell_reverse_tcp.bin
│  │      win32_shell_reverse_tcp.bin
│  │      win32_urldownload.bin
│  │      win32_wincalc.bin
│  │      win64_ob_msg_box_x64.asm
│  │      win64_ob_msg_box_x64.bin
│  │      win64_ob_msg_box_x64.hex
│  │      
│  └─src
│      ├─freebsd
│      │      hello.c
│      │      Makefile
│      │      README
│      │      x8664_hello_asm.S
│      │      
│      ├─linux
│      │  │  absolutepath.c
│      │  │  armeb_hello
│      │  │  armeb_hello_static
│      │  │  armeb_multithreading
│      │  │  armeb_puts
│      │  │  armeb_tcp_test
│      │  │  armeb_udp_test
│      │  │  arm_stat.c
│      │  │  cloexec_test.c
│      │  │  cwd.c
│      │  │  fetch_urandom.c
│      │  │  fetch_urandom_multiple_times.c
│      │  │  getdents.c
│      │  │  hello.c
│      │  │  hello.cpp
│      │  │  hello_mips32.s
│      │  │  hello_riscv.s
│      │  │  Makefile
│      │  │  mem_invalid_access.c
│      │  │  multithreading.c
│      │  │  patch_test.bin.c
│      │  │  patch_test.so.c
│      │  │  patch_test.so.h
│      │  │  path_traverse.c
│      │  │  posix_syscall.c
│      │  │  posix_syscall_execve.c
│      │  │  puts.c
│      │  │  README
│      │  │  sleep_hello.c
│      │  │  tcp_test.c
│      │  │  udp_test.c
│      │  │  vshttpd.c
│      │  │  
│      │  └─picohttpd
│      │          httpd.c
│      │          httpd.h
│      │          main.c
│      │          Makefile
│      │          picohttpd
│      │          readme.txt
│      │          
│      ├─macos
│      │      helloworld.c
│      │      README
│      │      x8664_hello.asm
│      │      x86_hello.asm
│      │      
│      ├─qnx
│      │      hello.c
│      │      hellosqrt.c
│      │      Makefile
│      │      README
│      │      
│      └─windows
│              argv.c
│              cmdln.c
│              file_upx.c
│              hello.c
│              MultiThread.c
│              NtQuerySystemInfo.c
│              README
│              return_main.c
│              
├─qiling
│  │  const.py
│  │  core.py
│  │  core_hooks.py
│  │  core_hooks_types.py
│  │  core_struct.py
│  │  exception.py
│  │  host.py
│  │  log.py
│  │  utils.py
│  │  __init__.py
│  │  
│  ├─arch
│  │  │  arch.py
│  │  │  arm.py
│  │  │  arm64.py
│  │  │  arm64_const.py
│  │  │  arm_const.py
│  │  │  arm_utils.py
│  │  │  cortex_m.py
│  │  │  cortex_m_const.py
│  │  │  mips.py
│  │  │  mips_const.py
│  │  │  msr.py
│  │  │  ppc.py
│  │  │  ppc_const.py
│  │  │  register.py
│  │  │  riscv.py
│  │  │  riscv64.py
│  │  │  riscv_const.py
│  │  │  utils.py
│  │  │  x86.py
│  │  │  x86_const.py
│  │  │  x86_utils.py
│  │  │  __init__.py
│  │  │  
│  │  └─evm
│  │      │  abc.py
│  │      │  abi.py
│  │      │  AUTHORS.TXT
│  │      │  constants.py
│  │      │  evm.py
│  │      │  exceptions.py
│  │      │  hooks.py
│  │      │  typing.py
│  │      │  validation.py
│  │      │  __init__.py
│  │      │  
│  │      ├─analysis
│  │      │      signatures.json
│  │      │      signatures.py
│  │      │      __init__.py
│  │      │      
│  │      ├─db
│  │      │  │  accesslog.py
│  │      │  │  account.py
│  │      │  │  atomic.py
│  │      │  │  batch.py
│  │      │  │  cache.py
│  │      │  │  diff.py
│  │      │  │  hash_trie.py
│  │      │  │  journal.py
│  │      │  │  keymap.py
│  │      │  │  slow_journal.py
│  │      │  │  storage.py
│  │      │  │  witness.py
│  │      │  │  __init__.py
│  │      │  │  
│  │      │  └─backends
│  │      │          base.py
│  │      │          memory.py
│  │      │          __init__.py
│  │      │          
│  │      ├─precompiles
│  │      │      blake2.py
│  │      │      ecadd.py
│  │      │      ecmul.py
│  │      │      ecpairing.py
│  │      │      ecrecover.py
│  │      │      identity.py
│  │      │      modexp.py
│  │      │      ripemd160.py
│  │      │      sha256.py
│  │      │      __init__.py
│  │      │      
│  │      ├─rlp
│  │      │      accounts.py
│  │      │      sedes.py
│  │      │      __init__.py
│  │      │      
│  │      ├─vm
│  │      │  │  code_stream.py
│  │      │  │  computation.py
│  │      │  │  dbgcui.py
│  │      │  │  debug.py
│  │      │  │  defaultconf.py
│  │      │  │  disassembler.py
│  │      │  │  evm.py
│  │      │  │  exec.py
│  │      │  │  execution_context.py
│  │      │  │  gas_meter.py
│  │      │  │  host.py
│  │      │  │  instruction.py
│  │      │  │  interrupt.py
│  │      │  │  memory.py
│  │      │  │  message.py
│  │      │  │  mnemonics.py
│  │      │  │  opcode.py
│  │      │  │  opcodes.py
│  │      │  │  opcode_values.py
│  │      │  │  stack.py
│  │      │  │  state.py
│  │      │  │  transaction_context.py
│  │      │  │  utils.py
│  │      │  │  vm.py
│  │      │  │  __init__.py
│  │      │  │  
│  │      │  ├─forks
│  │      │  │  │  __init__.py
│  │      │  │  │  
│  │      │  │  ├─berlin
│  │      │  │  │      computation.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─byzantium
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─constantinople
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      storage.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─frontier
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      transaction_context.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─homestead
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─istanbul
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      storage.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─muir_glacier
│  │      │  │  │      computation.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─petersburg
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  ├─spurious_dragon
│  │      │  │  │      computation.py
│  │      │  │  │      constants.py
│  │      │  │  │      opcodes.py
│  │      │  │  │      state.py
│  │      │  │  │      _utils.py
│  │      │  │  │      __init__.py
│  │      │  │  │      
│  │      │  │  └─tangerine_whistle
│  │      │  │          computation.py
│  │      │  │          constants.py
│  │      │  │          opcodes.py
│  │      │  │          state.py
│  │      │  │          __init__.py
│  │      │  │          
│  │      │  └─logic
│  │      │          arithmetic.py
│  │      │          block.py
│  │      │          call.py
│  │      │          comparison.py
│  │      │          context.py
│  │      │          duplication.py
│  │      │          flow.py
│  │      │          invalid.py
│  │      │          logging.py
│  │      │          memory.py
│  │      │          sha3.py
│  │      │          stack.py
│  │      │          storage.py
│  │      │          swap.py
│  │      │          system.py
│  │      │          __init__.py
│  │      │          
│  │      └─_utils
│  │          │  address.py
│  │          │  bn128.py
│  │          │  datatypes.py
│  │          │  generator.py
│  │          │  numeric.py
│  │          │  padding.py
│  │          │  transactions.py
│  │          │  __init__.py
│  │          │  
│  │          └─blake2  python希哈函数
│  │                  coders.py
│  │                  compression.py
│  │                  __init__.py
│  │                  
│  ├─cc
│  │      arm.py
│  │      intel.py
│  │      mips.py
│  │      ppc.py
│  │      riscv.py
│  │      __init__.py
│  │      
│  ├─debugger
│  │  │  debugger.py
│  │  │  disassember.py
│  │  │  utils.py
│  │  │  __init__.py
│  │  │  
│  │  ├─gdb
│  │  │  │  gdb.py
│  │  │  │  utils.py
│  │  │  │  xmlregs.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─xml
│  │  │      ├─a8086
│  │  │      │      gdb_init_real_mode.txt
│  │  │      │      i386-32bit.xml
│  │  │      │      target.xml
│  │  │      │      
│  │  │      ├─arm
│  │  │      │      arm-core.xml
│  │  │      │      arm-fpa.xml
│  │  │      │      arm-m-profile.xml
│  │  │      │      arm-vfpv2.xml
│  │  │      │      arm-vfpv3.xml
│  │  │      │      target.xml
│  │  │      │      xscale-iwmmxt.xml
│  │  │      │      
│  │  │      ├─arm64
│  │  │      │      aarch64-core.xml
│  │  │      │      aarch64-fpu.xml
│  │  │      │      target.xml
│  │  │      │      
│  │  │      ├─mips
│  │  │      │      mips-cp0.xml
│  │  │      │      mips-cpu.xml
│  │  │      │      mips-fpu.xml
│  │  │      │      target.xml
│  │  │      │      
│  │  │      ├─x86
│  │  │      │      32bit-avx.xml
│  │  │      │      32bit-avx512.xml
│  │  │      │      32bit-core.xml
│  │  │      │      32bit-linux.xml
│  │  │      │      32bit-mpx.xml
│  │  │      │      32bit-pkeys.xml
│  │  │      │      32bit-segments.xml
│  │  │      │      32bit-sse.xml
│  │  │      │      target.xml
│  │  │      │      
│  │  │      └─x8664
│  │  │              64bit-avx.xml
│  │  │              64bit-avx512.xml
│  │  │              64bit-core.xml
│  │  │              64bit-linux.xml
│  │  │              64bit-mpx.xml
│  │  │              64bit-pkeys.xml
│  │  │              64bit-segments.xml
│  │  │              64bit-sse.xml
│  │  │              target.xml
│  │  │              
│  │  └─qdb
│  │      │  const.py
│  │      │  context.py
│  │      │  memory.py
│  │      │  misc.py
│  │      │  qdb.py
│  │      │  README.md
│  │      │  utils.py
│  │      │  __init__.py
│  │      │  
│  │      ├─arch
│  │      │      arch.py
│  │      │      arch_arm.py
│  │      │      arch_mips.py
│  │      │      arch_x86.py
│  │      │      arch_x8664.py
│  │      │      __init__.py
│  │      │      
│  │      ├─branch_predictor
│  │      │      branch_predictor.py
│  │      │      branch_predictor_arm.py
│  │      │      branch_predictor_mips.py
│  │      │      branch_predictor_x86.py
│  │      │      branch_predictor_x8664.py
│  │      │      __init__.py
│  │      │      
│  │      └─render
│  │              render.py
│  │              render_arm.py
│  │              render_mips.py
│  │              render_x86.py
│  │              render_x8664.py
│  │              __init__.py
│  │              
│  ├─extensions
│  │  │  multitask.py
│  │  │  pipe.py
│  │  │  trace.py
│  │  │  winsdkapi.py
│  │  │  __init__.py
│  │  │  
│  │  ├─afl
│  │  │      afl.py
│  │  │      __init__.py
│  │  │      
│  │  ├─coverage
│  │  │  │  README.md
│  │  │  │  utils.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─formats
│  │  │          base.py
│  │  │          drcov.py
│  │  │          drcov_exact.py
│  │  │          history.py
│  │  │          __init__.py
│  │  │          
│  │  ├─idaplugin
│  │  │      qilingida.py
│  │  │      readme.md
│  │  │      __init__.py
│  │  │      
│  │  ├─mcu
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  ├─atmel
│  │  │  │      sam3x8e.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  ├─bes
│  │  │  │      bes2300.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  ├─gd32vf1
│  │  │  │      gd32vf103.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  ├─nxp
│  │  │  │      mk64f12.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  ├─stm32f1
│  │  │  │      stm32f103.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  └─stm32f4
│  │  │          stm32f401.py
│  │  │          stm32f405.py
│  │  │          stm32f407.py
│  │  │          stm32f410.py
│  │  │          stm32f411.py
│  │  │          stm32f412.py
│  │  │          stm32f413.py
│  │  │          stm32f415.py
│  │  │          stm32f417.py
│  │  │          stm32f423.py
│  │  │          stm32f427.py
│  │  │          stm32f429.py
│  │  │          stm32f437.py
│  │  │          stm32f439.py
│  │  │          stm32f446.py
│  │  │          stm32f469.py
│  │  │          stm32f479.py
│  │  │          __init__.py
│  │  │          
│  │  ├─r2
│  │  │      r2.py
│  │  │      __init__.py
│  │  │      
│  │  ├─report
│  │  │      report.py
│  │  │      __init__.py
│  │  │      
│  │  ├─sanitizers
│  │  │      heap.py
│  │  │      __init__.py
│  │  │      
│  │  └─tracing
│  │      │  README.md
│  │      │  utils.py
│  │      │  __init__.py
│  │      │  
│  │      └─formats
│  │              base.py
│  │              registers.py
│  │              tenet.py
│  │              __init__.py
│  │              
│  ├─hw
│  │  │  connectivity.py
│  │  │  hw.py
│  │  │  peripheral.py
│  │  │  __init__.py
│  │  │  
│  │  ├─analog
│  │  │      mk64f12_adc.py
│  │  │      sam3xa_adc.py
│  │  │      sam3xa_dac.py
│  │  │      sam3xa_pwm.py
│  │  │      stm32f1xx_adc.py
│  │  │      stm32f4xx_dac.py
│  │  │      __init__.py
│  │  │      
│  │  ├─char
│  │  │      gd32vf1xx_usart.py
│  │  │      mk64f12_uart.py
│  │  │      sam3xa_uart.py
│  │  │      sam3xa_uotghs.py
│  │  │      stm32f1xx_usart.py
│  │  │      stm32f4xx_usart.py
│  │  │      __init__.py
│  │  │      
│  │  ├─const
│  │  │      cm4_systick.py
│  │  │      gd32vf1xx_dma.py
│  │  │      gd32vf1xx_i2c.py
│  │  │      gd32vf1xx_rcu.py
│  │  │      gd32vf1xx_rtc.py
│  │  │      gd32vf1xx_spi.py
│  │  │      gd32vf1xx_timer.py
│  │  │      gd32vf1xx_usart.py
│  │  │      mk64f12_adc.py
│  │  │      mk64f12_ftm.py
│  │  │      mk64f12_mcg.py
│  │  │      mk64f12_port.py
│  │  │      mk64f12_spi.py
│  │  │      mk64f12_uart.py
│  │  │      sam3xa_adc.py
│  │  │      sam3xa_dac.py
│  │  │      sam3xa_pmc.py
│  │  │      sam3xa_spi.py
│  │  │      sam3xa_uart.py
│  │  │      sam3xa_uotghs.py
│  │  │      stm32f1xx_adc.py
│  │  │      stm32f1xx_dma.py
│  │  │      stm32f4xx_dma.py
│  │  │      stm32f4xx_eth.py
│  │  │      stm32f4xx_i2c.py
│  │  │      stm32f4xx_pwr.py
│  │  │      stm32f4xx_rtc.py
│  │  │      stm32f4xx_sdio.py
│  │  │      stm32f4xx_spi.py
│  │  │      stm32f4xx_tim.py
│  │  │      stm32f4xx_usart.py
│  │  │      stm32fxxx_rcc.py
│  │  │      __init__.py
│  │  │      
│  │  ├─dma
│  │  │      gd32vf1xx_dma.py
│  │  │      sam3xa_pdc.py
│  │  │      stm32f1xx_dma.py
│  │  │      stm32f4xx_dma.py
│  │  │      __init__.py
│  │  │      
│  │  ├─external_device
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  ├─lcd
│  │  │  │      const.py
│  │  │  │      lcd1602.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  └─oled
│  │  │          ssd1306.py
│  │  │          __init__.py
│  │  │          
│  │  ├─flash
│  │  │      sam3xa_efc.py
│  │  │      stm32f1xx_flash.py
│  │  │      stm32f4xx_flash.py
│  │  │      __init__.py
│  │  │      
│  │  ├─gpio
│  │  │      gd32vf1xx_gpio.py
│  │  │      hooks.py
│  │  │      mk64f12_gpio.py
│  │  │      mk64f12_port.py
│  │  │      sam3xa_pio.py
│  │  │      stm32f1xx_afio.py
│  │  │      stm32f1xx_gpio.py
│  │  │      stm32f4xx_gpio.py
│  │  │      __init__.py
│  │  │      
│  │  ├─i2c
│  │  │      gd32vf1xx_i2c.py
│  │  │      stm32f1xx_i2c.py
│  │  │      stm32f4xx_i2c.py
│  │  │      __init__.py
│  │  │      
│  │  ├─intc
│  │  │      cm3_nvic.py
│  │  │      cm4_nvic.py
│  │  │      cm_nvic.py
│  │  │      gd32vf1xx_eclic.py
│  │  │      stm32f1xx_exti.py
│  │  │      stm32f4xx_exti.py
│  │  │      __init__.py
│  │  │      
│  │  ├─math
│  │  │      gd32vf1xx_crc.py
│  │  │      stm32f4xx_crc.py
│  │  │      __init__.py
│  │  │      
│  │  ├─mem
│  │  │      cm_bitband.py
│  │  │      kinetis_bme.py
│  │  │      remap.py
│  │  │      __init__.py
│  │  │      
│  │  ├─misc
│  │  │      cm3_scb.py
│  │  │      cm4_scb.py
│  │  │      cm_scb.py
│  │  │      gd32vf1xx_rcu.py
│  │  │      mk64f12_mcg.py
│  │  │      mk64f12_sim.py
│  │  │      mk64f12_smc.py
│  │  │      mk64f12_wdog.py
│  │  │      sam3xa_wdt.py
│  │  │      stm32f1xx_rcc.py
│  │  │      stm32f4xx_dbg.py
│  │  │      stm32f4xx_rcc.py
│  │  │      stm32f4xx_rcc_derive.py
│  │  │      stm32f4xx_syscfg.py
│  │  │      __init__.py
│  │  │      
│  │  ├─net
│  │  │      stm32f4xx_eth.py
│  │  │      __init__.py
│  │  │      
│  │  ├─power
│  │  │      sam3xa_pmc.py
│  │  │      stm32f4xx_pwr.py
│  │  │      __init__.py
│  │  │      
│  │  ├─sd
│  │  │      stm32f4xx_sdio.py
│  │  │      __init__.py
│  │  │      
│  │  ├─spi
│  │  │      gd32vf1xx_spi.py
│  │  │      mk64f12_spi.py
│  │  │      sam3xa_spi.py
│  │  │      stm32f1xx_spi.py
│  │  │      stm32f4xx_spi.py
│  │  │      __init__.py
│  │  │      
│  │  ├─timer
│  │  │      cm3_systick.py
│  │  │      cm4_systick.py
│  │  │      cm_systick.py
│  │  │      gd32vf1xx_rtc.py
│  │  │      gd32vf1xx_timer.py
│  │  │      mk64f12_ftm.py
│  │  │      mk64f12_osc.py
│  │  │      mk64f12_rtc.py
│  │  │      sam3xa_tc.py
│  │  │      stm32f1xx_tim.py
│  │  │      stm32f4xx_rtc.py
│  │  │      stm32f4xx_tim.py
│  │  │      timer.py
│  │  │      __init__.py
│  │  │      
│  │  └─utils
│  │          access.py
│  │          bcd.py
│  │          serial.py
│  │          __init__.py
│  │          
│  ├─loader
│  │  │  blob.py
│  │  │  dos.py
│  │  │  elf.py
│  │  │  evm.py
│  │  │  loader.py
│  │  │  macho.py
│  │  │  mcu.py
│  │  │  pe.py
│  │  │  pe_uefi.py
│  │  │  __init__.py
│  │  │  
│  │  └─macho_parser
│  │          const.py
│  │          data.py
│  │          header.py
│  │          loadcommand.py
│  │          parser.py
│  │          utils.py
│  │          __init__.py
│  │          
│  ├─os
│  │  │  const.py
│  │  │  disk.py
│  │  │  fcall.py
│  │  │  filestruct.py
│  │  │  mapper.py
│  │  │  memory.py
│  │  │  os.py
│  │  │  path.py
│  │  │  stats.py
│  │  │  struct.py
│  │  │  thread.py
│  │  │  utils.py
│  │  │  __init__.py
│  │  │  
│  │  ├─blob
│  │  │      blob.py
│  │  │      __init__.py
│  │  │      
│  │  ├─dos
│  │  │  │  dos.py
│  │  │  │  utils.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─interrupts
│  │  │          int10.py
│  │  │          int13.py
│  │  │          int15.py
│  │  │          int16.py
│  │  │          int19.py
│  │  │          int1a.py
│  │  │          int20.py
│  │  │          int21.py
│  │  │          __init__.py
│  │  │          
│  │  ├─freebsd
│  │  │      const.py
│  │  │      freebsd.py
│  │  │      map_syscall.py
│  │  │      syscall.py
│  │  │      __init__.py
│  │  │      
│  │  ├─linux
│  │  │  │  fncc.py
│  │  │  │  function_hook.py
│  │  │  │  futex.py
│  │  │  │  linux.py
│  │  │  │  map_syscall.py
│  │  │  │  procfs.py
│  │  │  │  syscall.py
│  │  │  │  syscall_nums.py
│  │  │  │  thread.py
│  │  │  │  utils.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─kernel_api
│  │  │          hook.py
│  │  │          kernel_api.py
│  │  │          __init__.py
│  │  │          
│  │  ├─macos
│  │  │  │  const.py
│  │  │  │  fncc.py
│  │  │  │  kernel_func.py
│  │  │  │  mach_port.py
│  │  │  │  macos.py
│  │  │  │  map_syscall.py
│  │  │  │  structs.py
│  │  │  │  subsystems.py
│  │  │  │  syscall.py
│  │  │  │  task.py
│  │  │  │  thread.py
│  │  │  │  utils.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  ├─events
│  │  │  │      macos.py
│  │  │  │      macos_policy.py
│  │  │  │      macos_structs.py
│  │  │  │      __init__.py
│  │  │  │      
│  │  │  └─kernel_api
│  │  │          hook.py
│  │  │          kernel_api.py
│  │  │          __init__.py
│  │  │          
│  │  ├─mcu
│  │  │      const.py
│  │  │      mcu.py
│  │  │      __init__.py
│  │  │      
│  │  ├─posix
│  │  │  │  const.py
│  │  │  │  const_mapping.py
│  │  │  │  filestruct.py
│  │  │  │  posix.py
│  │  │  │  stat.py
│  │  │  │  structs.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─syscall
│  │  │          fcntl.py
│  │  │          futex.py
│  │  │          ioctl.py
│  │  │          mman.py
│  │  │          msg.py
│  │  │          net.py
│  │  │          personality.py
│  │  │          poll.py
│  │  │          prctl.py
│  │  │          ptrace.py
│  │  │          random.py
│  │  │          resource.py
│  │  │          sched.py
│  │  │          select.py
│  │  │          sendfile.py
│  │  │          shm.py
│  │  │          signal.py
│  │  │          socket.py
│  │  │          stat.py
│  │  │          syscall.py
│  │  │          sysctl.py
│  │  │          sysinfo.py
│  │  │          time.py
│  │  │          types.py
│  │  │          uio.py
│  │  │          unistd.py
│  │  │          utsname.py
│  │  │          wait.py
│  │  │          __init__.py
│  │  │          
│  │  ├─qnx
│  │  │      const.py
│  │  │      helpers.py
│  │  │      map_msgtype.py
│  │  │      map_syscall.py
│  │  │      message.py
│  │  │      qnx.py
│  │  │      structs.py
│  │  │      syscall.py
│  │  │      types.py
│  │  │      __init__.py
│  │  │      
│  │  ├─uefi
│  │  │  │  bs.py
│  │  │  │  const.py
│  │  │  │  context.py
│  │  │  │  ds.py
│  │  │  │  fncc.py
│  │  │  │  guids.csv
│  │  │  │  hob.py
│  │  │  │  PiMultiPhase.py
│  │  │  │  ProcessorBind.py
│  │  │  │  rt.py
│  │  │  │  smm.py
│  │  │  │  smst.py
│  │  │  │  st.py
│  │  │  │  type32.py
│  │  │  │  type64.py
│  │  │  │  uefi.py
│  │  │  │  UefiBaseType.py
│  │  │  │  UefiMultiPhase.py
│  │  │  │  UefiSpec.py
│  │  │  │  utils.py
│  │  │  │  __init__.py
│  │  │  │  
│  │  │  └─protocols
│  │  │          common.py
│  │  │          EfiLoadedImageProtocol.py
│  │  │          EfiSmmAccess2Protocol.py
│  │  │          EfiSmmBase2Protocol.py
│  │  │          EfiSmmCpuProtocol.py
│  │  │          EfiSmmSwDispatch2Protocol.py
│  │  │          PcdProtocol.py
│  │  │          __init__.py
│  │  │          
│  │  └─windows
│  │      │  api.py
│  │      │  clipboard.py
│  │      │  const.py
│  │      │  fiber.py
│  │      │  fncc.py
│  │      │  handle.py
│  │      │  registry.py
│  │      │  structs.py
│  │      │  thread.py
│  │      │  utils.py
│  │      │  wdk_const.py
│  │      │  windows.py
│  │      │  __init__.py
│  │      │  
│  │      └─dlls
│  │          │  advapi32.py
│  │          │  const.py
│  │          │  crypt32.py
│  │          │  mscoree.py
│  │          │  msi.py
│  │          │  msvbvm60.py
│  │          │  msvcrt.py
│  │          │  ntdll.py
│  │          │  ntoskrnl.py
│  │          │  ole32.py
│  │          │  oleaut32.py
│  │          │  shell32.py
│  │          │  shlwapi.py
│  │          │  ucrtbased.py
│  │          │  user32.py
│  │          │  wininet.py
│  │          │  wsock32.py
│  │          │  wudplatform.py
│  │          │  __init__.py
│  │          │  
│  │          └─kernel32
│  │                  consoleapi.py
│  │                  consoleapi2.py
│  │                  consoleapi3.py
│  │                  debugapi.py
│  │                  errhandlingapi.py
│  │                  fibersapi.py
│  │                  fileapi.py
│  │                  handleapi.py
│  │                  heapapi.py
│  │                  interlockedapi.py
│  │                  ioapiset.py
│  │                  libloaderapi.py
│  │                  memoryapi.py
│  │                  processenv.py
│  │                  processthreadsapi.py
│  │                  profileapi.py
│  │                  psapi.py
│  │                  stringapiset.py
│  │                  synchapi.py
│  │                  sysinfoapi.py
│  │                  timezoneapi.py
│  │                  tlhelp32.py
│  │                  winbase.py
│  │                  winnls.py
│  │                  winnt.py
│  │                  wow64apiset.py
│  │                  __init__.py
│  │                  
│  └─profiles
│          dos.ql
│          freebsd.ql
│          linux.ql
│          macos.ql
│          qnx.ql
│          uefi.ql
│          windows.ql
│          
└─tests
    │  README
    │  test_android.py
    │  test_blob.py
    │  test_debugger.py
    │  test_dos.py
    │  test_dos_exe.py
    │  test_edl.py
    │  test_elf.py
    │  test_elf_ko.py
    │  test_elf_multithread.py
    │  test_evm.py
    │  test_history.py
    │  test_macho.py
    │  test_macho.sh
    │  test_macho_kext.py
    │  test_mcu.py
    │  test_onlinux.sh
    │  test_pathutils.py
    │  test_pe.bat
    │  test_pe.py
    │  test_perf.py
    │  test_peshellcode.py
    │  test_pe_sys.py
    │  test_posix.py
    │  test_qdb.py
    │  test_qltool.py
    │  test_qnx.py
    │  test_r2.py
    │  test_riscv.py
    │  test_shellcode.py
    │  test_struct.py
    │  test_tendaac15_httpd.py
    │  test_uefi.py
    │  test_windows_debugger.py
    │  test_windows_stdio.py
    │  view_perf_results.py
    │  
    ├─profiles
    │      uboot_bin.ql
    │      windows_gandcrab_admin.ql
    │      windows_gandcrab_russian_keyboard.ql
    │      windows_gandcrab_user.ql
    │      
    └─qdb_scripts
            arm.qdb
            mips32el.qdb
            x86.qdb
            

```