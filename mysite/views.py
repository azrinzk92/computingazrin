from django.http import HttpResponse
from django.shortcuts import render
import Bio
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def transcription(request):
	return render(request, 'transcription.html')
    
def translation(request):
	return render(request, 'translation.html')
    
def gcpercentage(request):
	return render(request, 'gcpercentage.html')
    
def pairwisealignment(request):
	return render(request, 'pairwise.html')
    
def transcriptionresult(request):
    dna = Seq(request.GET['dnasequence'])
    mrna = dna.transcribe()
    return render(request, 'transcriptionresult.html', {'data':mrna, 'seqsatu':dna})
    
def translationresult(request):
    dnaa = Seq(request.GET['urutan'])
    seqres = dnaa.translate()
    return render(request, 'translationresult.html', {'datasatu':seqres, 'seqdua':dnaa})
    
def gcpercentageresult(request):
    dnab = request.GET['peratus']
    dnalen = len(dnab)
    aperc = int(((dnab.count('A')*100)/dnalen))
    tperc = int(((dnab.count('T')*100)/dnalen))
    gperc = int(((dnab.count('G')*100)/dnalen))
    cperc = int(((dnab.count('C')*100)/dnalen))
    gcres = int(GC(dnab))
    return render(request, 'gcpercentageresult.html', {'datadua':gcres, 'ares': aperc, 'tres': tperc, 'gres': gperc, 'cres': cperc})
    
def pairwiseresult(request):
    sequn = request.GET['urutansatu']
    seqdeux = request.GET['urutandua']
    alignments = pairwise2.align.globalxx(sequn, seqdeux)
    alignsun = format_alignment(*alignments[0])
    return render(request, 'pairwiseresult.html', {'datatiga':alignsun, 'firstdna':sequn, 'seconddna':seqdeux})  
    
def reversecomplement(request):
    return render(request, 'revcom.html')

def reversecomplementresult(request):
    seqtrois = Seq(request.GET['urutanterbalik'])
    revcomdna = seqtrois.reverse_complement()
    return render(request, 'revcomresult.html', {'dataempat':revcomdna, 'seqtiga':seqtrois})