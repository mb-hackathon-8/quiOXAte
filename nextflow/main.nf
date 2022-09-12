#!/usr/bin/env nextflow
nextflow.enable.dsl=2
version = '1.0'

// setup the analysis

inputdata = Channel.fromPath(params.inputdb)


process SETUP_FASTA {

    publisDir "${launchDir}",
    mode: 'copy'

    cache 'lenient'

    input:
        path(inputdb)
    output:
        path('combined.faa'), emit:combined
    
    script:
    """
    seqkit rmdup -s $inputdb | seqkit grep -v -r -n -p 'Prev'> combined.faa
    """
}




workflow {

    take:
        inputdata
    main:

        SETUP_FASTA( inputdata )


}