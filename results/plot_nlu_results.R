intent_results <- read.csv("~/catkin_ws/src/lh7-nlp/nlp_magic/src/rasa_project/results/intent_results.csv")

# for a split of 10%, plotting average F1 score across runs for each intent
split_10.f1 <- subset(intent_results, (split==10 & X.1=='f1-score'))

split_10.f1 = subset(split_10.f1, select = c(X, "greetings", "bye", "none", "affirmative", "deny", "show", "find", "pick.up", "move", pipeline))

split_10.f1.avg = aggregate(x=split_10.f1,
                            by = list(split_10.f1$pipeline),
                            FUN=mean)

split_10.f1.avg = subset(split_10.f1.avg, select = c("greetings", "bye", "none", "affirmative", "deny", "show", "find", "pick.up", "move", pipeline))
data.split_10.f1.avg <- melt(split_10.f1.avg,
                             id.vars=c("pipeline"),
                             measure.vars = c("greetings", "bye", "none", "affirmative", "deny", "show", "find", "pick.up", "move"))

intents_plot <- ggplot(data.split_10.f1.avg,aes(variable,value, fill=pipeline))
intents_plot + geom_col(position="dodge",
                            width=0.7) +
                labs(x="Intent",
                   y="F1 score (average across 2 runs)",
                   fill="RASA pipeline") +
                theme(legend.position = "top")
