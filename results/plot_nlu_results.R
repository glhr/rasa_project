intent_results <- read.csv("~/catkin_ws/src/lh7-nlp/nlp_magic/src/rasa_project/results/own_data/intent_results.csv")

# for a split of 10%, plotting average F1 score across runs for each intent
split_10.f1 <- subset(intent_results, (split==10 & X.1=='f1-score'))

split_10.f1 = subset(split_10.f1, select = c(X, greetings, bye, none, affirmative, deny, show, find, pick.up, move, clarify, pipeline))

split_10.f1.avg = aggregate(x=split_10.f1,
                            by = list(pipeline = split_10.f1$pipeline),
                            FUN=mean)

split_10.f1.avg = subset(split_10.f1.avg, select = c(greetings, bye, none, affirmative, deny, show, find, pick.up, move, clarify, pipeline))
data.split_10.f1.avg <- melt(split_10.f1.avg,
                             id.vars=c("pipeline"),
                             measure.vars = c("greetings", "bye", "none", "affirmative", "deny", "show", "find", "pick.up", "move", "clarify"))

intents_plot <- ggplot(data.split_10.f1.avg,
                       aes(x=reorder(variable, -value),
                           y=value,
                           fill=pipeline))
intents_plot + geom_col(position="dodge",
                            width=0.6) +
                labs(x="Intent",
                   y="F1 score (average across 3 runs)",
                   fill="RASA pipeline") +
                theme(legend.position = "right",
                      axis.text=element_text(size=12))
ggsave("own_data_intent-eval-0.1.pdf",width = 11, height=4)

#############################################

entity_results <- read.csv("~/catkin_ws/src/lh7-nlp/nlp_magic/src/rasa_project/results/own_data/entity_results.csv")

# for a split of 10%, plotting average F1 score across runs for each entity
split_10.f1 <- subset(entity_results, (split==10 & X.1=='f1-score'))

split_10.f1 = subset(split_10.f1, select = c(X, object_name, object_color, undefined_object, placement, pipeline))

split_10.f1.avg = aggregate(x=split_10.f1,
                            by = list(pipeline = split_10.f1$pipeline),
                            FUN=mean)

split_10.f1.avg = subset(split_10.f1.avg, select = c(object_name, object_color, undefined_object, placement, pipeline))
data.split_10.f1.avg <- melt(split_10.f1.avg,
                             id.vars=c("pipeline"),
                             measure.vars = c("object_name", "object_color", "placement"))

entitys_plot <- ggplot(data.split_10.f1.avg,
                       aes(reorder(variable, -value),
                           value,
                           fill=pipeline))
entitys_plot + geom_col(position="dodge",
                        width=0.5) +
  labs(x="Entity",
       y="F1 score (average across 3 runs)",
       fill="RASA pipeline") +
  theme(legend.position = "right",
        axis.text=element_text(size=12))
ggsave("own_data_entity-eval-0.1.pdf",width = 8, height=3)

