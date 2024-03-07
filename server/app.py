from fastapi import FastAPI
from routes.codex_assigment_route import router as CodexAssigmentRouter
from routes.codex_answer_route import router as CodexAnswerRouter
from routes.codecorr_assigment_route import router as CodecorrAssigmentRouter
from routes.codecorr_answer_route import router as CodecorrAnswerRouter

app = FastAPI(
    title='Code Program Assignment'
)


app.include_router(CodexAssigmentRouter, tags=["Code Execution Assignment"], prefix="/codexassigment")
app.include_router(CodexAnswerRouter, tags=["Code Execution Answer"] ,prefix="/codexanswer")
app.include_router(CodecorrAssigmentRouter, tags=["Code Correction Assignment"], prefix="/codecorrassigment")
app.include_router(CodecorrAnswerRouter, tags=["Code Correction Answer"] ,prefix="/codecorranswer")

