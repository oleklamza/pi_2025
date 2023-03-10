* = $C000

init  
        SEI                  ; set interrupt bit, make the CPU ignore interrupt requests
        LDA #%01111111       ; switch off interrupt signals from CIA-1
        STA $DC0D

        AND $D011            ; clear most significant bit of VIC's raster register
        STA $D011

        LDA $DC0D            ; acknowledge pending interrupts from CIA-1
        LDA $DD0D            ; acknowledge pending interrupts from CIA-2

        LDA #11              ; set rasterline where interrupt shall occur
        STA $D012

        LDA #<irq            ; set interrupt vectors, pointing to interrupt service routine below
        STA $0314
        LDA #>irq
        STA $0315

        LDA #%00000001       ; enable raster interrupt signals from VIC
        STA $D01A

        CLI                  ; clear interrupt flag, allowing the CPU to respond to interrupt requests
        RTS


irq
        LDX cnt
wait    
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP

        DEX
        BNE wait

        INC cnt

        LDY #0
loop    
        LDX #52
pause   
        DEX
        BNE pause

        LDA colors,Y
        STA $D021

        INY
        CPY #40
        BNE loop

        ASL $D019

        JMP $EA31

colors  .BYTE $0A,$07,$01,$0d,$03,$05,$07,$0D,$05,$0A
        .BYTE $07,$01,$0d,$03,$05,$07,$0D,$05,$0A,$07
        .BYTE $0A,$07,$01,$0d,$03,$05,$07,$0D,$05,$0A
        .BYTE $0A,$07,$01,$0d,$03,$05,$07,$0D,$05,$0A
cnt     .BYTE 0
