MAIN = applsm
#MAIN = usenix2019_v3.1

all: pdf

pdf: ${MAIN}.pdf

${MAIN}.pdf: *.tex
	pdflatex -interaction nonstopmode ${MAIN}.tex

bibtex:
	pdflatex ${MAIN}.tex
	bibtex ${MAIN}.aux
	pdflatex ${MAIN}.tex
	pdflatex ${MAIN}.tex

clean:
	rm -f ./${MAIN}.pdf
	rm -f ./${MAIN}.ps
	rm -f ./${MAIN}.out
	rm -f ./${MAIN}.blg
	rm -f ./${MAIN}.log
	rm -f ./${MAIN}.bbl
	rm -f ./${MAIN}.aux
	rm -f ./${MAIN}.bcf
	rm -f ./${MAIN}.run.xml
	rm -f ./comment.cut
